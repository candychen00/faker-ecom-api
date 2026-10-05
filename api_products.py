from fastapi import APIRouter, Depends
from starlette import status
from auth import verify_api_key

from models import products

from sqlalchemy import inspect, text
from database import engine
from schema import ProductCreate

import random


router = APIRouter(
    prefix="/products", 
    tags=["products"],
    dependencies=[Depends(verify_api_key)],
)


@router.get("/tables", status_code=status.HTTP_200_OK)
def show_tables(schema: str = "public"):
    inspector = inspect(engine)
    return {"schema": schema, "tables": inspector.get_table_names(schema=schema)}


# @router.delete("/tables/{t_name}", status_code=status.HTTP_204_NO_CONTENT)
# def drop_table(t_name: str, schema: str = "public"):
#     with engine.begin() as conn:
#         stmt = f'DROP TABLE IF EXISTS "{schema}"."{t_name}"'
#         conn.execute(text(stmt))


@router.get("/generate_all_products", status_code=status.HTTP_200_OK)
def generate_all_products():
    product_fruits = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Mango', 'Blueberry', 'Peach', 'Pineapple']
    product_categories = ['Juice', 'Jam', 'Dried Snacks', 'Smoothie', 'Gummies']

    product_id = -1
    all_products = []
    for fruit in product_fruits:
        for category in product_categories:
            product_id+=1
            all_products.append(
                {
                    'product_id': product_id,
                    'fruit': fruit,
                    'category': category,
                    'price': round(random.uniform(10,20),2),
                }
            )
    return all_products


@router.get("/all_products", status_code=status.HTTP_200_OK)
def get_all_products():
    with engine.connect() as conn:
        stmt = products.select()
        result = conn.execute(stmt)
        return result.mappings().all()


@router.post("/create_products", status_code=status.HTTP_201_CREATED)
def create_products(prod_data: list[ProductCreate]):
    with engine.begin() as conn:
        stmt = products.insert()
        data = [i.model_dump() for i in prod_data]

        conn.execute(stmt, data)


@router.delete("/delete_products", status_code=status.HTTP_204_NO_CONTENT)
def delete_products(ids: list[int]):
    with engine.begin() as conn:
        stmt = products.delete().where(products.c.product_id.in_(ids))
        conn.execute(stmt)
