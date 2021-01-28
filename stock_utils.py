# print("Hi")
# 
# # import stock_info module from yahoo_fin
# from yahoo_fin import stock_info as si
# 
# # get live price of Apple
# si.get_live_price("aapl")
#  
# # or Amazon
# si.get_live_price("amzn")
#  
# # # or any other ticker
# # si.get_live_price(ticker)
# 
# print("done")


import yfinance as yf


# data = yf.download("ABEV3.SA", start="2020-03-01", end="2020-03-30")
data = yf.download("ABR", start="2020-03-01", end="2020-03-30")
print(data)