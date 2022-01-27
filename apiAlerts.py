'''
Algorithm / Flow:

1. get SYMBOLS from /v1/symbols
2. for each SYMBOL (if not ALL), calculate current price using /v1/pricefeed
3. use /v2/ticker/:symbol to calculate 24hr_average (add all , divide by 24)
4. use /v2/ticker/:symbol to calculate standard_deviation (use above formula)
5. use 24hr_average, standard_deviation to calculate percentage relative standard deviation
6. if standard_deviation percentage is more than INPUT (eg 1%):
7. print output in specified format
'''

import requests
import statistics
from datetime import datetime
class apiAlerts:

    def __init__(self, currency:str, deviation:int):
        self.currency = currency
        self.deviation = deviation
        self.base_url_v1 = "https://api.sandbox.gemini.com/v1"        
        self.base_url_v2 = "https://api.sandbox.gemini.com/v2"

    def generateAlert(self):
        symbols = self.getSymbols()
        pricefeed = self.getPricefeed()

        for s in symbols:
            v = self.getClosingData(s)
            last_price = pricefeed[s.upper()]

            list_of_floats = []
            for item in v["changes"]:
                list_of_floats.append(float(item))
            
            average = self.getAverage(list_of_floats)
            change = self.getStandardDeviation(list_of_floats)
            sdev = self.getRelativeStandardDeviation(average, change)

            output = {
                        "timestamp": "{}".format(datetime.now()),
                        "level": "INFO",
                        "trading_pair": "{}".format(s),
                        "deviation": True,
                        "data": {
                            "last_price": "{}".format(last_price),
                            "average": "{}".format(average),
                            "change": "{}".format(change),
                            "sdev": "{}".format(sdev)
                        }
                     }
                        
            if sdev > self.deviation:
                print(output)

    def getSymbols(self):
        if(self.currency == "ALL"):
            response = requests.get(self.base_url_v1 + "/symbols")
            symbols = response.json()
            return symbols
        else:
            arr = []
            arr.append(self.currency)
            return arr
    
    def getPricefeed(self):
        response = requests.get(self.base_url_v1 + "/pricefeed")
        a = dict()
        for r in response.json():
            a[r["pair"]] = r["price"]
        return a

    def getClosingData(self, s):
        response = requests.get(self.base_url_v2 + "/ticker/{}".format(s))
        return response.json()
    
    def getAverage(self, data):
        average = statistics.fmean(data)
        return average
    
    def getStandardDeviation(self, data):
        standard_deviation = statistics.stdev(data)
        return standard_deviation
    
    def getRelativeStandardDeviation(self, average, standard_deviation):
        rsd = round(standard_deviation*100/average,2)
        return rsd