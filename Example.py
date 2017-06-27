from CryptoCompare import CryptoCompare
import time

cc = CryptoCompare()
currency = 'ETH'


historyDataDay = cc.histoMinute(currency)

for x in range(len(historyDataDay)):
    highPrice = historyDataDay[x]['high']
    time = historyDataDay[x]['time']
    print('High price of {0} at timestamp {1} = {2}'.format(currency,time,highPrice))
