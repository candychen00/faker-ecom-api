from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
import api_products, api_customers
from database import create_tables

from contextlib import asynccontextmanager

import os
from dotenv import load_dotenv


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(api_products.router)
app.include_router(api_customers.router)


load_dotenv()
API_KEY = os.getenv("API_KEY")

api_key_header = APIKeyHeader(name="X-API-Key")

def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key",
        )

    return api_key
