import pandas as pd
from logger_setup import setup_logging
from fetch_stock_data import fetch_stock_data
from json_loader import load_config


def main():
    config = load_config()

    logger = setup_logging()

    all_dataframes = []

    for stock in config["stocks"]:
        try:
            logger.info(f"Fetching data for {stock['ticker_symbol']}")
            stock_to_fetch = fetch_stock_data(stock['ticker_symbol'], stock['company_name'])

            all_dataframes.append(stock_to_fetch)
        except Exception as e:
            logger.error(f"Failed to fetch {stock['ticker_symbol']} : {e}")
            continue
    
    if not all_dataframes:
        logger.error("No data fetched for any stock")
        return

    combine = pd.concat(all_dataframes, ignore_index=True)
    combine.to_csv(config['temp_data_path'], index=False)
    logger.info(f"Saved {len(combine)} rows to {config['temp_data_path']}")

if __name__ == "__main__":
    main()