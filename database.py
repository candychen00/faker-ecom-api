from sqlalchemy import MetaData, create_engine

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(f"{DATABASE_URL}", echo=True)

meta = MetaData()

def create_tables():
    meta.create_all(engine)