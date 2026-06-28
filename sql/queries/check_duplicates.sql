SELECT ticker, trade_date, COUNT(*)
FROM stock_prices
GROUP BY ticker, trade_date
HAVING COUNT(*) > 1;
