from logger_setup import setup_logging
from db_connection import get_snowflake_connection
import pandas as pd
from json_loader import load_config

def main():
    logger = setup_logging()
    conn = get_snowflake_connection()
    logger.info("Connecting to Snowflake")
    cursor = conn.cursor()

    config = load_config()

    read_csv = pd.read_csv(config['temp_data_path'])

    for index, row in read_csv.iterrows():
        logger.info(f"Fetching data for {row['ticker']}")
        try:
            cursor.execute(
                "MERGE INTO stock_prices AS target USING (SELECT %s AS ticker, %s AS company_name, %s AS trade_date, %s AS open_price, %s AS close_price, %s AS high_price, %s AS low_price, %s AS volume) AS source ON target.ticker = source.ticker AND target.trade_date = source.trade_date WHEN NOT MATCHED THEN INSERT (ticker, company_name, trade_date, open_price, close_price, high_price, low_price, volume) VALUES (source.ticker, source.company_name, source.trade_date, source.open_price, source.close_price, source.high_price, source.low_price, source.volume)",
                (row['ticker'], row['company_name'], row['trade_date'], row['open_price'], row['close_price'], row['high_price'], row['low_price'], row['volume'])
            )

        except Exception as e:
            logger.error(e)
            continue

    conn.commit()
    logger.info(f"Successfully loaded {len(read_csv)} rows into snowflake")
    logger.info("Closing Snowflake connection and cursor connection")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

