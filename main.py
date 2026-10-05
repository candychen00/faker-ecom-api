from fastapi import FastAPI
import api_products, api_customers
from database import create_tables

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(api_products.router)
app.include_router(api_customers.router)
