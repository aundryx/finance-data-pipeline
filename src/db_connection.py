import psycopg2 
from dotenv import load_dotenv
import os

load_dotenv()

# Local postgres database connection function
def get_db_connection():
    conn = psycopg2.connect(
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT")
    )

    return conn

# AWS RDS postgres database connection function
def get_rds_connection():
    conn = psycopg2.connect (
        dbname = os.getenv("RDS_DB_NAME"),
        user = os.getenv("RDS_DB_USER"),
        password = os.getenv("RDS_DB_PASSWORD"),
        host = os.getenv("RDS_DB_HOST"),
        port = os.getenv("RDS_DB_PORT")
    )

    return conn

