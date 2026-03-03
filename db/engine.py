from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, declarative_base

host = getenv("DB_HOST")
port = getenv("DB_PORT")
user = getenv("DB_USER")
password = getenv("DB_PASSWORD")
database = getenv("DB_NAME")

if not all([host, port, user, password, database]):
    raise ValueError("Database connection parameters are not fully set in environment variables.")

connection_string = f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(connection_string)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()