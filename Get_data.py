import yfinance as yf

# List of stock symbols
stocks = ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'TSLA']

# Dictionary to store data
stock_data = {}

# Fetch the data
for stock in stocks:
    print(f"Fetching data for {stock}...")
    # Download historical stock data
    data = yf.download(stock, start='2014-01-01', end='2024-04-01')
    # Save data to dictionary
    stock_data[stock] = data

# Save each stock's data to a CSV file
for stock, data in stock_data.items():
    filename = f"{stock}_daily_data.csv"
    data.to_csv(filename)
    print(f"Data for {stock} saved to {filename}")

print("All data fetching and saving complete.")
