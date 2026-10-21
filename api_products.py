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
    # product_fruits = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Mango', 'Blueberry', 'Peach', 'Pineapple']
    # product_categories = ['Juice', 'Jam', 'Dried Snacks', 'Smoothie', 'Gummies']

    # product_id = -1
    # all_products = []
    # for fruit in product_fruits:
    #     for category in product_categories:
    #         product_id+=1
    #         all_products.append(
    #             {
    #                 'product_id': product_id,
    #                 'fruit': fruit,
    #                 'category': category,
    #                 'price': round(random.uniform(10,20),2),
    #             }
    #         )
    return [
        {
            "product_id": 0,
            "fruit": "Apple",
            "category": "Juice",
            "price": 13.89
        },
        {
            "product_id": 1,
            "fruit": "Apple",
            "category": "Jam",
            "price": 14.87
        },
        {
            "product_id": 2,
            "fruit": "Apple",
            "category": "Dried Snacks",
            "price": 16.79
        },
        {
            "product_id": 3,
            "fruit": "Apple",
            "category": "Smoothie",
            "price": 13.38
        },
        {
            "product_id": 4,
            "fruit": "Apple",
            "category": "Gummies",
            "price": 12.72
        },
        {
            "product_id": 5,
            "fruit": "Banana",
            "category": "Juice",
            "price": 12.47
        },
        {
            "product_id": 6,
            "fruit": "Banana",
            "category": "Jam",
            "price": 17.01
        },
        {
            "product_id": 7,
            "fruit": "Banana",
            "category": "Dried Snacks",
            "price": 17.56
        },
        {
            "product_id": 8,
            "fruit": "Banana",
            "category": "Smoothie",
            "price": 10.52
        },
        {
            "product_id": 9,
            "fruit": "Banana",
            "category": "Gummies",
            "price": 12.97
        },
        {
            "product_id": 10,
            "fruit": "Orange",
            "category": "Juice",
            "price": 19.23
        },
        {
            "product_id": 11,
            "fruit": "Orange",
            "category": "Jam",
            "price": 11.85
        },
        {
            "product_id": 12,
            "fruit": "Orange",
            "category": "Dried Snacks",
            "price": 18.88
        },
        {
            "product_id": 13,
            "fruit": "Orange",
            "category": "Smoothie",
            "price": 11.99
        },
        {
            "product_id": 14,
            "fruit": "Orange",
            "category": "Gummies",
            "price": 15.31
        },
        {
            "product_id": 15,
            "fruit": "Strawberry",
            "category": "Juice",
            "price": 19.82
        },
        {
            "product_id": 16,
            "fruit": "Strawberry",
            "category": "Jam",
            "price": 10.52
        },
        {
            "product_id": 17,
            "fruit": "Strawberry",
            "category": "Dried Snacks",
            "price": 16.39
        },
        {
            "product_id": 18,
            "fruit": "Strawberry",
            "category": "Smoothie",
            "price": 17.98
        },
        {
            "product_id": 19,
            "fruit": "Strawberry",
            "category": "Gummies",
            "price": 14.18
        },
        {
            "product_id": 20,
            "fruit": "Mango",
            "category": "Juice",
            "price": 12.09
        },
        {
            "product_id": 21,
            "fruit": "Mango",
            "category": "Jam",
            "price": 17.48
        },
        {
            "product_id": 22,
            "fruit": "Mango",
            "category": "Dried Snacks",
            "price": 12.63
        },
        {
            "product_id": 23,
            "fruit": "Mango",
            "category": "Smoothie",
            "price": 10.08
        },
        {
            "product_id": 24,
            "fruit": "Mango",
            "category": "Gummies",
            "price": 10.35
        },
        {
            "product_id": 25,
            "fruit": "Blueberry",
            "category": "Juice",
            "price": 16.65
        },
        {
            "product_id": 26,
            "fruit": "Blueberry",
            "category": "Jam",
            "price": 18.26
        },
        {
            "product_id": 27,
            "fruit": "Blueberry",
            "category": "Dried Snacks",
            "price": 12.59
        },
        {
            "product_id": 28,
            "fruit": "Blueberry",
            "category": "Smoothie",
            "price": 14.78
        },
        {
            "product_id": 29,
            "fruit": "Blueberry",
            "category": "Gummies",
            "price": 16.67
        },
        {
            "product_id": 30,
            "fruit": "Peach",
            "category": "Juice",
            "price": 13.44
        },
        {
            "product_id": 31,
            "fruit": "Peach",
            "category": "Jam",
            "price": 13.68
        },
        {
            "product_id": 32,
            "fruit": "Peach",
            "category": "Dried Snacks",
            "price": 11.23
        },
        {
            "product_id": 33,
            "fruit": "Peach",
            "category": "Smoothie",
            "price": 13.81
        },
        {
            "product_id": 34,
            "fruit": "Peach",
            "category": "Gummies",
            "price": 18.05
        },
        {
            "product_id": 35,
            "fruit": "Pineapple",
            "category": "Juice",
            "price": 12.12
        },
        {
            "product_id": 36,
            "fruit": "Pineapple",
            "category": "Jam",
            "price": 13.03
        },
        {
            "product_id": 37,
            "fruit": "Pineapple",
            "category": "Dried Snacks",
            "price": 16.12
        },
        {
            "product_id": 38,
            "fruit": "Pineapple",
            "category": "Smoothie",
            "price": 19
        },
        {
            "product_id": 39,
            "fruit": "Pineapple",
            "category": "Gummies",
            "price": 16.75
        }
    ]


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
