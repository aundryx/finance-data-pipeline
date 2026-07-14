import logging
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
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
