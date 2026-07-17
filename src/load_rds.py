import pandas as pd
from logger_setup import setup_logging
from db_connection import get_rds_connection
from json_loader import load_config


def main():
    logger = setup_logging()
    conn = get_rds_connection()
    logger.info("Connected to AWS PostgreSQL RDS")
    cursor = conn.cursor()

    csv_temp_path = load_config()

    read_csv = pd.read_csv(csv_temp_path['temp_data_path'])

    for index, row in read_csv.iterrows():
        logger.info(f"Fetching data for {row['ticker']}")
        try:
            cursor.execute(
                "INSERT INTO stock_prices (ticker, company_name, trade_date, open_price, close_price, high_price, low_price, volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (ticker, trade_date) DO NOTHING",
                (row['ticker'], row['company_name'], row['trade_date'], row['open_price'], row['close_price'], row['high_price'], row['low_price'], row['volume'])
            )
        
        except Exception as e:
            logger.error(e)
            continue

    conn.commit()
    logger.info(f"Successfully loaded {len(read_csv)} rows into RDS")
    logger.info("Closing RDS connection and cursor connection")
    cursor.close()
    conn.close()
    

if __name__ == "__main__":
    main()




        
    






