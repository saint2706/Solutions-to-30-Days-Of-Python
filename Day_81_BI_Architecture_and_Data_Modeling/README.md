# Day 81 – BI Architecture and Data Modeling

## Why it matters

Business intelligence teams translate raw data into governed insights. A clear architecture
keeps ingestion, storage, and analytics aligned so analysts can trust their data assets and
ship faster.

## Agenda

- Map core data architecture layers, from ingestion pipelines to semantic models.
- Compare centralized warehouses, flexible lakes, and focused marts for BI delivery.
- Evaluate modeling trade-offs between star and snowflake patterns.
- Clarify fact/dimension roles, calculated measures, and semantic model governance.

## Star schema example

The `build_star_schema_example` helper in `solutions.py` models a retail analytics star schema
with a `fact_sales` table and conformed date, customer, product, and store dimensions. Use the
[Power BI star schema guidance](https://learn.microsoft.com/power-bi/guidance/star-schema)
for a diagrammed walkthrough that mirrors the classroom example.

## Snowflake schema example

The `build_snowflake_schema_example` helper extends the retail model by normalizing the
product hierarchy into dedicated tables. Compare the metadata with the
[Snowflake TPC-DS reference models](https://docs.snowflake.com/en/user-guide/sample-data-tpcds)
to see how snowflaked product dimensions appear in SQL DDL.

## Classroom resources

- `lesson.py` prints the roadmap topics and walks through both schema examples with references.
- `solutions.py` exposes grouped topic metadata plus helper functions for converting schema
  examples into structured dictionaries suitable for tests, slides, or demos.
- `tests/test_day_81.py` (added in this task) ensures the helpers surface all expected titles and
  schema metadata.
