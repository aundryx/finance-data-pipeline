import logging 
import os
import json
from fetch_stock_data import fetch_stock_data

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
    logger = setup_logging() 
    logger.info("Pipeline started")

    stocks = load_config()
    logger.info(f"Loaded config: {len(stocks['stocks'])} stocks to fetch")


if __name__ == "__main__":
    main()








