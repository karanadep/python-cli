import requests, json

base_url = "https://api.sandbox.gemini.com/v1"
base_url = "https://api.sandbox.gemini.com/v2"

# returns list of symbols
# response = requests.get(base_url + "/symbols")
# symbols = response.json()
# for s in symbols:
#     print(s)
    
# Response is a list of objects, one for each pair,with the following fields:
#     {
#         "pair":"BTCUSD",
#         "price":"9500.00",
#         "percentChange24h": "5.23"
#     },
# response = requests.get(base_url + "/pricefeed")
# prices = response.json()
# print(prices)

# This will return the trades that have executed since the specified timestamp. Timestamps are either seconds or milliseconds since the epoch (1970-01-01). See the Data Types section about timestamp for information on this.
#   {
#     "timestamp": 1547146811,
#     "timestampms": 1547146811357,
#     "tid": 5335307668,
#     "price": "3610.85",
#     "amount": "0.27413495",
#     "exchange": "gemini",
#     "type": "buy"
#   },
# response = requests.get(base_url + "/trades/btcusd")
# btcusd_trades = response.json()
# print(btcusd_trades)

# This endpoint retrieves time-intervaled data for the provided symbol.
# GET https://api.gemini.com/v2/candles/:symbol/:time_frame

response = requests.get(base_url + "/candles/BTCUSD/1hr")
btc_candle_data = response.json()
print(btc_candle_data)


def CalculateStandardDeviation():
# Price Deviation - Generate an alert if the current price is more than one standard deviation from the 24hr average

    return True