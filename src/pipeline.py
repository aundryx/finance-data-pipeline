import logging 
import os
import json
from fetch_stock_data import fetch_stock_data

def setup_logging():
    os.makedirs("logs", exist_ok=True) # Creates a folder directory called logs if it doesn't exist

    # This define the the format of logging messages and the date format
    # The logging messages will include the timestamp, log level, and the actual message
    # The date format is set to "YYYY-MM-DD HH:MM:SS"
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    file_handler = logging.FileHandler("logs/pipeline.log") # This creates a file handler that writes log messages to a file named "pipeline.log" in the "logs" directory
    file_handler.setFormatter(formatter) # This sets the formatter for the file handler to the formatter defined earlier

    console_handler = logging.StreamHandler() # This creates a console handler that outputs log messages to the console/terminal
    console_handler.setFormatter(formatter) # This sets the formatter for the console handler to the formatter defined earlier

    # This creates our logger, set the logging level to INFO, and add the file and console handlers to it
    logger = logging.getLogger("stock_pipeline")
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def load_config():
    with open("config.json", "r") as f:
        config = json.load(f)
    return config

def main():
    logger = setup_logging() 
    logger.info("Pipeline started")

    stocks = load_config()
    logger.info(f"Loaded config: {len(stocks['stocks'])} stocks to fetch")


if __name__ == "__main__":
    main()








