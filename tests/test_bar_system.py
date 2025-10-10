"""Tests para el módulo ``mypackage.bar_system``."""

import os
import sys
from decimal import Decimal

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mypackage import BarSystem


@pytest.fixture
def sistema_bar() -> BarSystem:
    sistema = BarSystem(mesas=[1, 2], moneda="USD")
    sistema.agregar_item_inventario("CERV", "Cerveza artesanal", 3.5, 50, tipo="producto")
    sistema.agregar_item_inventario("EMP", "Empanada", 2.25, 30, tipo="producto")
    sistema.agregar_item_inventario("LIM", "Limones", 0.2, 100, tipo="insumo")
    return sistema


def test_reabastecimiento_actualiza_stock(sistema_bar: BarSystem) -> None:
    actualizado = sistema_bar.reabastecer("CERV", 10)
    assert actualizado.cantidad == Decimal("60")


def test_venta_rapida_descuenta_stock_y_registra_venta(sistema_bar: BarSystem) -> None:
    venta = sistema_bar.venta_rapida({"CERV": 2, "EMP": 1})
    assert venta.tipo == "rapida"
    assert venta.total == Decimal("9.25")
    assert sistema_bar.obtener_item("CERV").cantidad == Decimal("48")
    assert sistema_bar.obtener_item("EMP").cantidad == Decimal("29")


def test_agregar_consumo_mesa_y_cerrar_generan_venta(sistema_bar: BarSystem) -> None:
    sistema_bar.agregar_consumo_mesa(1, {"CERV": 3})
    sistema_bar.agregar_consumo_mesa(1, [("EMP", 2)])
    assert sistema_bar.total_mesa(1) == Decimal("15.00")
    venta = sistema_bar.cerrar_mesa(1)
    assert venta.tipo == "mesa"
    assert venta.mesa == "1"
    assert venta.total == Decimal("15.00")
    assert "1" not in sistema_bar.mesas_abiertas()


def test_no_permite_vender_mas_del_stock_disponible(sistema_bar: BarSystem) -> None:
    with pytest.raises(ValueError):
        sistema_bar.venta_rapida({"CERV": 200})


def test_consumo_insumos_restringido_a_tipo_insumo(sistema_bar: BarSystem) -> None:
    sistema_bar.consumir_insumo({"LIM": 5})
    assert sistema_bar.obtener_item("LIM").cantidad == Decimal("95")
    with pytest.raises(ValueError):
        sistema_bar.consumir_insumo({"CERV": 1})


def test_resumen_ventas_suma_mesas_y_rapidas(sistema_bar: BarSystem) -> None:
    sistema_bar.venta_rapida({"CERV": 2})
    sistema_bar.agregar_consumo_mesa(2, {"EMP": 3})
    sistema_bar.cerrar_mesa(2)
    sistema_bar.consumir_insumo({"LIM": 2})  # no suma al resumen
    assert sistema_bar.resumen_ventas() == Decimal("13.75")
