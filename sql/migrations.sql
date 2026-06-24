-- Migration: Added unique constraint to stock_prices table to prevent duplicate entries based on ticker and trade_date
-- Date: 2024-06-25

ALTER TABLE stock_prices
ADD CONSTRAINT unique_ticker_date UNIQUE (ticker, trade_date);