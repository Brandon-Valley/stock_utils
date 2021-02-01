import yfinance as yf

 
# # data = yf.download("ABEV3.SA", start="2020-03-01", end="2020-03-30")
# data = yf.download("ABR", start="2020-03-01", end="2020-03-30")
# print(data)

 
data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = "AAPL",
 
        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "1d",
 
        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1m",
 
        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',
 
        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,
 
        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,
 
        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,
 
        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )

# all data for given ticker
print(data)
# print(type(data))

print('-----------------------------------------')


close_prices = data['Close']
print('close_prices: ', close_prices)
print('close_prices[0]: ', close_prices[0])
print('latest stock price  --  close_prices[0]: ', close_prices[-1])
# print('latest stock price  --  close_prices[0]: ', type(close_prices[-1]))
# last_close_price = close_prices[Datetime[0]]
# print(last_close_price)


