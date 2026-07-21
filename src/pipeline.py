from fetch_stock_data import fetch_stock_data
from db_connection import get_rds_connection, get_snowflake_connection
from logger_setup import setup_logging
from json_loader import load_config


def main():
    logger = setup_logging() 

    conn = get_rds_connection()
    logger.info("Connected to AWS Postgres database")
    conn_snowflake = get_snowflake_connection()
    logger.info("Connected to Snowflake")

    cursor = conn.cursor()
    cursor_snowflake = conn_snowflake.cursor()

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

                cursor_snowflake.execute(
                    "MERGE INTO stock_prices AS target USING (SELECT %s AS ticker, %s AS company_name, %s AS trade_date, %s AS open_price, %s AS close_price, %s AS high_price, %s AS low_price, %s AS volume) AS source ON target.ticker = source.ticker AND target.trade_date = source.trade_date WHEN NOT MATCHED THEN INSERT (ticker, company_name, trade_date, open_price, close_price, high_price, low_price, volume) VALUES (source.ticker, source.company_name, source.trade_date, source.open_price, source.close_price, source.high_price, source.low_price, source.volume)",
                    (row['ticker'], row['company_name'], row['trade_date'], row['open_price'], row['close_price'], row['high_price'], row['low_price'], row['volume'])
                )

            conn.commit()
            conn_snowflake.commit()
            logger.info(f"Successfully loaded {len(stock_to_fetch)} rows for {stock['ticker_symbol']}")

        except Exception as e:
            logger.error(e)
            continue


    cursor.close() 
    conn.close()
    cursor_snowflake.close()
    conn_snowflake.close()
    logger.info("Pipeline completed")
        

if __name__ == "__main__":
    main()








