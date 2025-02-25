import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def fetch_stock_data(tickers, period='1y'):
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data[ticker] = stock.history(period=period)['Close']
    return pd.DataFrame(data)

def plot_stock_data(data):
    plt.figure(figsize=(14, 7))
    for column in data.columns:
        plt.plot(data.index, data[column], label=column)
    plt.title('Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']  # Add more stock tickers as needed
    period = '1y'  # You can change the period to '1mo', '6mo', '2y', etc.
    stock_data = fetch_stock_data(tickers, period)
    plot_stock_data(stock_data)