from sqlalchemy import Table, Column, Integer, String, DateTime, Float
from database import meta

customers = Table(
    "customers",
    meta,
    Column("customer_id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("email", String, nullable=False),
    Column("state", String, nullable=False),
    Column("signup_date", DateTime(timezone=True), nullable=False),
)

products = Table(
    "products",
    meta,
    Column("product_id", Integer, nullable=False),
    Column("fruit", String, nullable=False),
    Column("category", String, nullable=False),
    Column("price", Float, nullable=False),
)