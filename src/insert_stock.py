from db_connection import get_db_connection


conn = get_db_connection()
print("Connected successfully!")

cur = conn.cursor()
cur.execute(
    "INSERT INTO stock_prices (ticker, company_name, trade_date, open_price, close_price, high_price, low_price, volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    ("MYNLD", "Maynilad Water Services, Inc.", "2026-06-19", 22.45, 22.40, 22.70, 21.70, 110390900)
)

conn.commit()
cur.close()
conn.close()