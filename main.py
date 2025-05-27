import yfinance as yf  
import pandas as pd  

# Fetch AAPL stock data  
data = yf.download("AAPL", start="2023-01-01", end="2024-05-30")  

# Save to CSV  
data.to_csv("stock_data.csv")  
print("✅ Data saved to stock_data.csv!")  
