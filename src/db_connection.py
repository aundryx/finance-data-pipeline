import psycopg2 
from dotenv import load_dotenv
import os
import snowflake.connector

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

# Snowflake connection function
def get_snowflake_connection():
    conn = snowflake.connector.connect(
        user = os.getenv("SNOWFLAKE_USER"),
        account = os.getenv("SNOWFLAKE_ACCOUNT"),
        password = os.getenv("SNOWFLAKE_PASSWORD"),
        database = os.getenv("SNOWFLAKE_DATABASE"),
        schema = os.getenv("SNOWFLAKE_SCHEMA"),
        warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
        login_timeout = 60
        network_timeout = 60
    )

    return conn

