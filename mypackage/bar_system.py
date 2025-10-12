"""Sistema de gestión para bares.

Este módulo implementa un conjunto de clases para controlar las ventas de un
bar tanto en mesas como en ventas rápidas de mostrador. También mantiene el
estado del inventario de productos e insumos, permitiendo registrar
reabastecimientos y consumos internos.

La API está pensada para usarse desde scripts o aplicaciones de línea de
comandos y proporciona objetos ricos en información que pueden serializarse o
mostrarse en interfaces gráficas.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from typing import Iterable, Iterator, List, Mapping, MutableMapping, Optional, Sequence, Tuple, Union
from uuid import uuid4

DecimalLike = Union[str, int, float, Decimal]


def _to_decimal(value: DecimalLike) -> Decimal:
    """Convierte un valor numérico a :class:`~decimal.Decimal` de forma segura."""

    if isinstance(value, Decimal):
        return value
    return Decimal(str(value))


def _quantize_currency(value: Decimal) -> Decimal:
    """Redondea un valor monetario a dos decimales usando ``ROUND_HALF_UP``."""

    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


@dataclass(frozen=True)
class InventoryItem:
    """Representa un artículo del inventario de productos o insumos."""

    sku: str
    nombre: str
    unidad_precio: Decimal
    cantidad: Decimal
    unidad_medida: str = "unidades"
    tipo: str = "producto"  # producto o insumo

    def restock(self, cantidad: DecimalLike) -> "InventoryItem":
        """Retorna una copia con la cantidad incrementada."""

        incremento = _to_decimal(cantidad)
        if incremento <= 0:
            raise ValueError("La cantidad a reponer debe ser mayor que cero.")
        return replace(self, cantidad=self.cantidad + incremento)

    def consume(self, cantidad: DecimalLike) -> "InventoryItem":
        """Retorna una copia con la cantidad decrementada."""

        decremento = _to_decimal(cantidad)
        if decremento <= 0:
            raise ValueError("La cantidad a consumir debe ser mayor que cero.")
        if decremento > self.cantidad:
            raise ValueError(
                f"Stock insuficiente para {self.sku}: disponible {self.cantidad}, "
                f"solicitado {decremento}."
            )
        return replace(self, cantidad=self.cantidad - decremento)


@dataclass(frozen=True)
class SaleLine:
    """Detalle de un producto vendido."""

    sku: str
    nombre: str
    cantidad: Decimal
    precio_unitario: Decimal

    @property
    def total(self) -> Decimal:
        return _quantize_currency(self.precio_unitario * self.cantidad)


@dataclass(frozen=True)
class SaleRecord:
    """Representa una venta realizada en el bar."""

    identificador: str
    tipo: str  # "rapida" o "mesa"
    fecha: datetime
    lineas: Tuple[SaleLine, ...]
    mesa: Optional[str] = None
    nota: Optional[str] = None

    @property
    def total(self) -> Decimal:
        monto = sum((linea.total for linea in self.lineas), Decimal("0"))
        return _quantize_currency(monto)


@dataclass
class TableSession:
    """Mantiene el estado de consumo de una mesa."""

    identificador: str
    abierta: bool = False
    abierta_en: Optional[datetime] = None
    lineas: List[SaleLine] = field(default_factory=list)

    def abrir(self) -> None:
        if self.abierta:
            raise ValueError(f"La mesa {self.identificador} ya está abierta.")
        self.abierta = True
        self.abierta_en = datetime.now(tz=timezone.utc)

    def cerrar(self) -> None:
        if not self.abierta:
            raise ValueError(f"La mesa {self.identificador} no está abierta.")
        self.abierta = False
        self.abierta_en = None
        self.lineas.clear()


class BarSystem:
    """Controlador principal del sistema de bar."""

    def __init__(self, mesas: Iterable[Union[str, int]], moneda: str = "USD") -> None:
        mesas_iter = list(mesas)
        if not mesas_iter:
            raise ValueError("Debe proporcionar al menos una mesa para iniciar el sistema.")
        self.moneda = moneda
        self._inventario: MutableMapping[str, InventoryItem] = {}
        self._mesas: MutableMapping[str, TableSession] = {
            str(identificador): TableSession(str(identificador)) for identificador in mesas_iter
        }
        self._ventas: List[SaleRecord] = []

    # ------------------------------------------------------------------
    # Gestión de inventario
    # ------------------------------------------------------------------
    def agregar_item_inventario(
        self,
        sku: str,
        nombre: str,
        precio_unitario: DecimalLike,
        cantidad_inicial: DecimalLike,
        unidad_medida: str = "unidades",
        tipo: str = "producto",
    ) -> InventoryItem:
        """Registra un nuevo artículo en el inventario."""

        if sku in self._inventario:
            raise ValueError(f"El SKU {sku} ya existe en el inventario.")
        item = InventoryItem(
            sku=str(sku),
            nombre=nombre,
            unidad_precio=_quantize_currency(_to_decimal(precio_unitario)),
            cantidad=_to_decimal(cantidad_inicial),
            unidad_medida=unidad_medida,
            tipo=tipo,
        )
        if item.cantidad < 0:
            raise ValueError("La cantidad inicial no puede ser negativa.")
        self._inventario[item.sku] = item
        return item

    def reabastecer(self, sku: str, cantidad: DecimalLike) -> InventoryItem:
        """Incrementa el inventario de un artículo existente."""

        item = self._obtener_item(sku)
        actualizado = item.restock(cantidad)
        self._inventario[item.sku] = actualizado
        return actualizado

    def consumir_insumo(self, items: Union[Mapping[str, DecimalLike], Sequence[Tuple[str, DecimalLike]]], nota: Optional[str] = None) -> None:
        """Registra el uso interno de insumos sin generar una venta."""

        lineas = list(self._preparar_lineas(items, tipo_requerido="insumo"))
        # El consumo de insumos solo afecta el inventario; mantener un registro
        # permite auditar desde ``obtener_historial_inventario``.
        venta = SaleRecord(
            identificador=str(uuid4()),
            tipo="consumo",
            fecha=datetime.now(tz=timezone.utc),
            lineas=tuple(lineas),
            nota=nota,
        )
        self._ventas.append(venta)

    def obtener_item(self, sku: str) -> InventoryItem:
        """Devuelve una copia inmutable del artículo solicitado."""

        return replace(self._obtener_item(sku))

    def _obtener_item(self, sku: str) -> InventoryItem:
        try:
            return self._inventario[str(sku)]
        except KeyError as exc:  # pragma: no cover - mensaje explicativo
            raise KeyError(f"El SKU {sku} no existe en el inventario.") from exc

    def estado_inventario(self) -> List[InventoryItem]:
        """Obtiene una instantánea del inventario actual."""

        return [replace(item) for item in self._inventario.values()]

    # ------------------------------------------------------------------
    # Gestión de mesas
    # ------------------------------------------------------------------
    def abrir_mesa(self, identificador: Union[str, int]) -> None:
        mesa = self._obtener_mesa(identificador)
        mesa.abrir()

    def cerrar_mesa(self, identificador: Union[str, int]) -> SaleRecord:
        mesa = self._obtener_mesa(identificador)
        if not mesa.abierta:
            raise ValueError(f"La mesa {mesa.identificador} no está abierta.")
        if not mesa.lineas:
            raise ValueError(f"La mesa {mesa.identificador} no tiene consumos registrados.")
        venta = SaleRecord(
            identificador=str(uuid4()),
            tipo="mesa",
            fecha=datetime.now(tz=timezone.utc),
            lineas=tuple(mesa.lineas),
            mesa=mesa.identificador,
        )
        self._ventas.append(venta)
        mesa.cerrar()
        return venta

    def agregar_consumo_mesa(
        self,
        identificador: Union[str, int],
        items: Union[Mapping[str, DecimalLike], Sequence[Tuple[str, DecimalLike]]],
    ) -> List[SaleLine]:
        mesa = self._obtener_mesa(identificador)
        if not mesa.abierta:
            mesa.abrir()
        lineas = list(self._preparar_lineas(items))
        mesa.lineas.extend(lineas)
        return [replace(linea) for linea in lineas]

    def total_mesa(self, identificador: Union[str, int]) -> Decimal:
        mesa = self._obtener_mesa(identificador)
        monto = sum((linea.total for linea in mesa.lineas), Decimal("0"))
        return _quantize_currency(monto)

    def mesas_abiertas(self) -> List[str]:
        return [mesa.identificador for mesa in self._mesas.values() if mesa.abierta]

    # ------------------------------------------------------------------
    # Ventas
    # ------------------------------------------------------------------
    def venta_rapida(
        self,
        items: Union[Mapping[str, DecimalLike], Sequence[Tuple[str, DecimalLike]]],
        nota: Optional[str] = None,
    ) -> SaleRecord:
        lineas = tuple(self._preparar_lineas(items))
        venta = SaleRecord(
            identificador=str(uuid4()),
            tipo="rapida",
            fecha=datetime.now(tz=timezone.utc),
            lineas=lineas,
            nota=nota,
        )
        self._ventas.append(venta)
        return venta

    def historial_ventas(self) -> List[SaleRecord]:
        return list(self._ventas)

    def resumen_ventas(self) -> Decimal:
        monto = sum((venta.total for venta in self._ventas if venta.tipo in {"rapida", "mesa"}), Decimal("0"))
        return _quantize_currency(monto)

    # ------------------------------------------------------------------
    # Utilidades internas
    # ------------------------------------------------------------------
    def _obtener_mesa(self, identificador: Union[str, int]) -> TableSession:
        try:
            return self._mesas[str(identificador)]
        except KeyError as exc:  # pragma: no cover - mensaje explicativo
            raise KeyError(f"La mesa {identificador} no existe en el sistema.") from exc

    def _preparar_lineas(
        self,
        items: Union[Mapping[str, DecimalLike], Sequence[Tuple[str, DecimalLike]]],
        tipo_requerido: Optional[str] = None,
    ) -> Iterator[SaleLine]:
        normalizados = list(_normalizar_items(items))
        if not normalizados:
            raise ValueError("Debe proporcionar al menos un artículo.")
        # Validar disponibilidad antes de afectar el inventario
        for sku, cantidad in normalizados:
            item = self._obtener_item(sku)
            if tipo_requerido and item.tipo != tipo_requerido:
                raise ValueError(
                    f"El artículo {sku} es de tipo {item.tipo} y se requiere {tipo_requerido}."
                )
            if cantidad > item.cantidad:
                raise ValueError(
                    f"Stock insuficiente para {sku}: disponible {item.cantidad}, solicitado {cantidad}."
                )

        lineas: List[SaleLine] = []
        for sku, cantidad in normalizados:
            item = self._obtener_item(sku)
            actualizado = item.consume(cantidad)
            self._inventario[item.sku] = actualizado
            lineas.append(
                SaleLine(
                    sku=item.sku,
                    nombre=item.nombre,
                    cantidad=_to_decimal(cantidad),
                    precio_unitario=item.unidad_precio,
                )
            )
        return iter(lineas)


def _normalizar_items(
    items: Union[Mapping[str, DecimalLike], Sequence[Tuple[str, DecimalLike]]]
) -> Iterator[Tuple[str, Decimal]]:
    if isinstance(items, Mapping):
        iterable = items.items()
    else:
        iterable = items
    for registro in iterable:
        if isinstance(registro, Mapping):
            sku = registro.get("sku")
            cantidad = registro.get("cantidad")
        else:
            sku, cantidad = registro
        if sku is None:
            raise ValueError("Cada artículo debe incluir un SKU.")
        cantidad_decimal = _to_decimal(cantidad)
        if cantidad_decimal <= 0:
            raise ValueError("Las cantidades deben ser mayores que cero.")
        yield str(sku), cantidad_decimal
