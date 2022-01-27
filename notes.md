# Implement monitoring alerts using Gemini public API 

Link to API docs: https://docs.gemini.com/rest-api.

## Problem statement
For each of the symbols (ie. currency pairs) that Gemini trades you must generate an alert for the following condition:
```
Price Deviation - Generate an alert if the current price is more than one standard deviation from the 24hr average
```

## Output

### The alert should be a JSON formatted log line that highlights -
```
Timestamp in ISO8601 format (2006-31-10T15:00:00-0500)

Log level - (ie. INFO for regular output. ERROR for upstream errors, and logical/math errors, DEBUG for extra data that is not required for user consumption)

Trading Pair: BTCUSD/ETHUSD/BTCETH/etc.

Deviation: true/false boolean indicating if there is a price deviation or not

Data: additional data regarding the log, i.e. if there was an upstream ERROR, what it was, or if there was a price deviation, what the details of that deviation were

Last Price: a float object that indicates what the last price was

Average Price: average price over the requested time period

Deviation percentage: a float object that indicates the deviation as a percentage

Price change value: a float that object that indicates the deviation as a notional value
```