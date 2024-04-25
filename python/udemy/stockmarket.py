import requests

STOCK_ENDOPOINT = "https://www.alphavantage.co/query"
stock_params = {
	"function" : "TIME_SERIES_INTRADAY",
	"symbol" : "IBM",
	"interval" : "5min",
	"apikey" : "demo"
	}

response = requests.get(STOCK_ENDOPOINT, params=stock_params)
data = response.json()['Time Series (5min)']
data_price = data['2024-04-23 19:55:00']
print(data_price)
