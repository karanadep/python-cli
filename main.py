import argparse
from datetime import datetime
from apiAlerts import apiAlerts

# cli to pass arguments
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "{} - AlertingTool - INFO - Parsing args".format(datetime.now()))

    parser.add_argument("-c","--currency",dest='CURRENCY', default="btcusd", help="The currency trading pair, or ALL", type=str)
    parser.add_argument("-d","--deviation",dest="DEVIATION", default=1, help="percentage threshold for deviation", type=int)

    args = parser.parse_args()

    o = apiAlerts(args.CURRENCY, args.DEVIATION)
    o.generateAlert()