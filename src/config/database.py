import os
from dotenv import load_dotenv
from database import sqlite_handler, postgres_handler

ROOT_DIR = os.getcwd()

load_dotenv()

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE", "")
POSTGRES_USER = os.getenv("POSTGRES_USER", "")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")


sqlite = sqlite_handler.SQLiteHandler(os.path.join(ROOT_DIR, "database", "fourel_ai.db"))

postgres = postgres_handler.PostgresHandler(
    database=POSTGRES_DATABASE,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT
)

