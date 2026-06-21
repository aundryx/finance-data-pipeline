from db_connection import get_db_connection
from fetch_stock_data import fetch_stock_data

conn = get_db_connection()
print("Connected successfully!")

cur = conn.cursor()

history_reset = fetch_stock_data("AAPL", "Apple Inc.")

for index, row in history_reset.iterrows():
    cur.execute(
        "INSERT INTO stock_prices (ticker, company_name, trade_date, open_price, close_price, high_price, low_price, volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (row["ticker"], row["company_name"], row["trade_date"], row["open_price"], row["close_price"], row["high_price"], row["low_price"], row["volume"])
    )

conn.commit()
cur.close() 
conn.close()