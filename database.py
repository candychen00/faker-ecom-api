from sqlalchemy import MetaData, create_engine

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy 2.1 defaults "postgresql://" to psycopg (v3); we install psycopg2.
if DATABASE_URL and DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://", 1)

engine = create_engine(f"{DATABASE_URL}", echo=True)

meta = MetaData()

def create_tables():
    meta.create_all(engine)