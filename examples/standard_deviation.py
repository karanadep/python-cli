'''
current_price = 10
standard_deviation = 2
standard_average24hr = 14

examples
$ ./apiAlerts.py -c btcusd -d 1 | jq .
{
  "timestamp": "2021-11-15T18:25:43.511Z",
  "level": "INFO",
  "trading_pair": "btcusd",
  "deviation": true,
  "data": {
    "last_price": "64381.98",
    "average": "65196.09",
    "change": "765.67",
    "sdev": "1.2"
  }
}

$ ./apiAlerts.py -c ethusd -d 1 | jq .
{
  "timestamp": "2021-11-15T18:25:43.511Z",
  "level": "INFO",
  "trading_pair": "ethusd",
  "deviation": true,
  "data": {
    "last_price": "4607.69",
    "average": "4661.36",
    "change": "53.67",
    "sdev": "1.1"
  }
}

# current_price, standard_deviation, 24hr_average
how to get current price for symbol ? 
- https://api.sandbox.gemini.com/v1/pricefeed

how to get standard_deviation for symbol ? 
- 
import statistics
sample = [1,2,3,4,5,5,5,5,10]
standard_deviation = statistics.stdev(sample)
print(standard_deviation)
# Returns 2.55

how to get 24hr_average for symbol ? 
- 

what is percentChange24h ?
(Ending price - starting price)/(Starting price) = %change. You can make this calculation over any time period (hours, days, minutes, months, years) as long as you specify. If a stock is $100 now, and then in 10 minutes its $105, then it represents a 5% increase in 10 minutes. That's all there is to it.


Algorithm / Flow:

1. get SYMBOLS from /v1/symbols
2. for each SYMBOL (if not ALL), calculate current price using /v1/pricefeed
3. use /v2/ticker/:symbol to calculate 24hr_average (add all , divide by 24)
4. use /v2/ticker/:symbol to calculate standard_deviation (use above formula)
5. use 24hr_average, standard_deviation to calculate percentage relative standard deviation
6. if standard_deviation percentage is more than INPUT (eg 1%):
7. print output in specified format

'''

import statistics
sample = [
    "9365.1",
    "9386.16",
    "9373.41",
    "9322.56",
    "9268.89",
    "9265.38",
    "9245",
    "9231.43",
    "9235.88",
    "9265.8",
    "9295.18",
    "9295.47",
    "9310.82",
    "9335.38",
    "9344.03",
    "9261.09",
    "9265.18",
    "9282.65",
    "9260.01",
    "9225",
    "9159.5",
    "9150.81",
    "9118.6",
    "9148.01"
  ]

# https://www.youtube.com/watch?v=-MJ_kOlYmRk&ab_channel=CodeFather
# https://www.chem.tamu.edu/class/fyp/keeney/stddev.pdf

list_of_floats = []
for item in sample:
    list_of_floats.append(float(item))

print(list_of_floats)
standard_deviation = statistics.stdev(list_of_floats)
print("standard deviation price - Price change value - {}".format(standard_deviation))

# calculate average
average = statistics.fmean(list_of_floats)
print("average price - Average Price - {}".format(average))

# relative standard deviation (RSD) is often times more convenient. It is expressed in percent and is obtained by
# multiplying the standard deviation by 100 and dividing this product by the average.
print("standard deviation percentage - Deviation percentage - {}".format(round(standard_deviation*100/average,2)))

# Standard Deviation, s: 71.756056730678
# Count, N:	24
# Sum, Σx:	222411.34
# Mean, x̄:	9267.1391666667
# Variance, s2: 	5148.9316775362
