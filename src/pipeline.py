import logging 
import os
import json
from fetch_stock_data import fetch_stock_data
from db_connection import get_db_connection


BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
CONFIG_PATH = os.path.join(BASE_DIR, "..", "config.json") 
logs_dir = os.path.join(BASE_DIR, "..", "logs")

def setup_logging():
    os.makedirs(logs_dir, exist_ok=True) 

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    file_handler = logging.FileHandler(os.path.join(logs_dir, "pipeline.log")) 
    file_handler.setFormatter(formatter) 

    console_handler = logging.StreamHandler() 
    console_handler.setFormatter(formatter)

   
    logger = logging.getLogger("stock_pipeline")
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def load_config():
    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)
    return config

def main():
    conn = get_db_connection()
    cursor = conn.cursor()

    logger = setup_logging() 

    config = load_config()

    logger.info(f"Starting ETL pipeline for {len(config['stocks'])} stocks")

    for stock in config["stocks"]:
        logger.info(f"Fetching data for {stock['ticker_symbol']}")

        try:
            stock_to_fetch = fetch_stock_data(stock['ticker_symbol'], stock['company_name'])
            logger.info(f"Transforming data for {stock['ticker_symbol']}")

            for index, row in stock_to_fetch.iterrows():
                cursor.execute(
                    "INSERT INTO stock_prices (ticker, company_name, trade_date, open_price, close_price, high_price, low_price, volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (ticker, trade_date) DO NOTHING",
                    (row['ticker'], row['company_name'], row['trade_date'], row['open_price'], row['close_price'], row['high_price'], row['low_price'], row['volume']) 
                )

            conn.commit()
            logger.info(f"Successfully loaded {len(stock_to_fetch)} rows for {stock['ticker_symbol']}")

        except Exception as e:
            logger.error(e)
            continue

    cursor.close() 
    conn.close()
    logger.info("Pipeline completed")
        

if __name__ == "__main__":
    main()








