from db_connection import get_db_connection
from fetch_stock_data import fetch_stock_data

conn = get_db_connection()
print("Connected successfully!")

cur = conn.cursor()

stocks_to_fetch = [
    {"ticker_symbol": "PLTR", "company_name": "Palantir Technologies Inc."},
    {"ticker_symbol": "GOOG", "company_name": "Alphabet Inc."},
    {"ticker_symbol": "MSFT", "company_name": "Microsoft Corporation"},
    {"ticker_symbol": "META", "company_name": "Meta Platforms, Inc."},
    {"ticker_symbol": "TSLA", "company_name": "Tesla, Inc."},
    {"ticker_symbol": "NVDA", "company_name": "NVIDIA Corporation"},
]

for stocks in stocks_to_fetch:
    history_reset = fetch_stock_data(stocks["ticker_symbol"], stocks["company_name"])
    for index, row in history_reset.iterrows():
        cur.execute(
            "INSERT INTO stock_prices (ticker, company_name, trade_date, open_price, close_price, high_price, low_price, volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (row["ticker"], row["company_name"], row["trade_date"], row["open_price"], row["close_price"], row["high_price"], row["low_price"], row["volume"])
        )

conn.commit()
cur.close() 
conn.close()