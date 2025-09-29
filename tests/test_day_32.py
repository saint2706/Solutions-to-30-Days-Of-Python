"""Unit tests for the Day 32 dependency-injected database helpers."""

import os
import sys
from unittest import mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_32_Other_Databases.other_databases import (  # noqa: E402
    execute_sql_query,
    find_documents,
    insert_documents,
    upsert_sales_forecast,
)


def test_execute_sql_query_uses_client_factory_and_closes_resources():
    credentials = {"host": "localhost", "user": "analyst"}
    connection = mock.Mock()
    cursor = connection.cursor.return_value
    cursor.fetchall.return_value = [("North", 10)]
    client_factory = mock.Mock(return_value=connection)

    rows = execute_sql_query(
        client_factory,
        "SELECT * FROM sales WHERE region = %s",
        credentials=credentials,
        parameters=("North",),
    )

    assert rows == [("North", 10)]
    client_factory.assert_called_once_with(credentials)
    connection.cursor.assert_called_once()
    cursor.execute.assert_called_once_with("SELECT * FROM sales WHERE region = %s", ("North",))
    cursor.fetchall.assert_called_once()
    cursor.close.assert_called_once()
    connection.close.assert_called_once()
    assert not connection.commit.called


def test_execute_sql_query_commits_when_requested():
    credentials = {"host": "localhost"}
    connection = mock.Mock()
    connection.cursor.return_value.fetchall.return_value = []
    client_factory = mock.Mock(return_value=connection)

    execute_sql_query(
        client_factory,
        "UPDATE sales SET revenue = revenue + 100",
        credentials=credentials,
        commit=True,
    )

    connection.commit.assert_called_once()


def test_upsert_sales_forecast_executes_all_rows_and_commits():
    credentials = {"host": "db.internal"}
    connection = mock.Mock()
    cursor = connection.cursor.return_value
    client_factory = mock.Mock(return_value=connection)

    forecast_rows = [
        ("North", "2024-10", 125000),
        ("South", "2024-10", 99000),
    ]

    upsert_sales_forecast(client_factory, credentials=credentials, forecast_rows=forecast_rows)

    client_factory.assert_called_once_with(credentials)
    assert cursor.execute.call_count == len(forecast_rows)
    executed_queries = {call.args[1] for call in cursor.execute.call_args_list}
    assert executed_queries == set(forecast_rows)
    connection.commit.assert_called_once()
    cursor.close.assert_called_once()
    connection.close.assert_called_once()


def test_find_documents_passes_filter_and_projection():
    mongo_client = mock.MagicMock()
    database = mongo_client.__getitem__.return_value
    collection = database.__getitem__.return_value
    expected_docs = [{"_id": 1, "region": "EMEA"}]
    collection.find.return_value = iter(expected_docs)

    docs = find_documents(
        mongo_client,
        database="analytics",
        collection="sales",
        filter_query={"region": "EMEA"},
        projection={"_id": 1, "region": 1},
    )

    mongo_client.__getitem__.assert_called_once_with("analytics")
    database.__getitem__.assert_called_once_with("sales")
    collection.find.assert_called_once_with({"region": "EMEA"}, {"_id": 1, "region": 1})
    assert docs == expected_docs


def test_find_documents_defaults_to_empty_filter():
    mongo_client = mock.MagicMock()
    database = mongo_client.__getitem__.return_value
    collection = database.__getitem__.return_value
    collection.find.return_value = iter([{"region": "APAC"}])

    docs = find_documents(mongo_client, database="analytics", collection="sales")

    collection.find.assert_called_once_with({})
    assert docs == [{"region": "APAC"}]


def test_insert_documents_returns_inserted_ids_and_handles_empty_inputs():
    mongo_client = mock.MagicMock()
    database = mongo_client.__getitem__.return_value
    collection = database.__getitem__.return_value
    insert_result = mock.Mock(inserted_ids=[1, 2])
    collection.insert_many.return_value = insert_result

    inserted_ids = insert_documents(
        mongo_client,
        database="analytics",
        collection="sales",
        documents=[{"region": "North"}, {"region": "South"}],
    )

    mongo_client.__getitem__.assert_called_once_with("analytics")
    database.__getitem__.assert_called_once_with("sales")
    collection.insert_many.assert_called_once()
    assert inserted_ids == [1, 2]

    mongo_client_empty = mock.MagicMock()
    result = insert_documents(
        mongo_client_empty,
        database="analytics",
        collection="sales",
        documents=[],
    )

    assert result == []
    mongo_client_empty.__getitem__.assert_not_called()
