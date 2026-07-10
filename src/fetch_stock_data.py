import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker_symbol, company_name):

    ticker = yf.Ticker(ticker_symbol) # Extraction

    result = ticker.history(period="10d") # Extraction

    history_reset = result.reset_index() # Transformation

    history_reset["Date"] = history_reset["Date"].dt.date # Transformation

    history_reset["ticker"] = ticker_symbol # Transformation

    history_reset["company_name"] = company_name # Transformation

    history_reset = history_reset.drop(columns=["Dividends", "Stock Splits"]) # Transformation

    history_reset = history_reset.rename(columns={
        'Date' : 'trade_date', 
        'Open' : 'open_price', 
        'High' : 'high_price', 
        'Low' : 'low_price', 
        'Close' : 'close_price', 
        'Volume' : 'volume'
    }) # Transformation

    history_reset["open_price"] = history_reset["open_price"].round(2) # Transformation
    history_reset["high_price"] = history_reset["high_price"].round(2)  # Transformation
    history_reset["low_price"] = history_reset["low_price"].round(2) # Transformation
    history_reset["close_price"] = history_reset["close_price"].round(2) # Transformation

    return history_reset

