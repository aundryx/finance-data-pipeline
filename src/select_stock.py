from db_connection import get_db_connection
import pandas as pd

conn = get_db_connection()
print("Connected successfully!")

cur = conn.cursor()
cur.execute("SELECT * FROM stock_prices")

results = cur.fetchall()

df = pd.DataFrame(results, columns=['id', 'ticker', 'company_name', 'trade_date', 'open_price', 'close_price', 'high_price', 'low_price', 'volume'])
print(df)

cur.close()
conn.close()