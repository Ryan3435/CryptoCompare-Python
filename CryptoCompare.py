import urllib
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json
import time

class CryptoCompare(object):
	
	
    def query(self, url):
        req = urllib2.Request(url)
        response = json.loads(urllib2.urlopen(req).read())
        
        if(type(response) != "None"):
            return response
        else:
            print(url)
            print("Failed to contact CryptoCompare api")		
            return -1
	
    def price(self,currency,inTermsOf='BTC'):
        url = 'https://min-api.cryptocompare.com/data/price?fsym='
        url += currency + '&tsyms='
        url += inTermsOf
        return self.query(url)
        
    def priceHistorical(self,currency,inTermsOf='BTC'):
        url = 'https://min-api.cryptocompare.com/data/pricehistorical?fsym='
        url += currency + '&tsyms='
        url += inTermsOf
        return self.query(url)
    
    def generateAvg(self,currency,inTermsOf='USD',markets='Coinbase,Kraken,Bitstamp,Bitfinex'):
        url = 'https://min-api.cryptocompare.com/data/generateAvg?fsym='
        url += currency + '&tsym='
        url += inTermsOf + '&markets=' + markets
        return self.query(url)
    
    def histoMinute(self, currency, baseCurrency = 'BTC', limit = 60, aggregate = 0, toTs = ""):
        url = 'https://min-api.cryptocompare.com/data/histominute?fsym='
        url += currency + '&tsym='
        url += baseCurrency + '&limit='
        url += str(limit) + '&aggregate=' + str(aggregate)
        url += toTs
        return self.query(url)["Data"]
        
    def histoHour(self, currency, baseCurrency = 'BTC', limit = 60, aggregate = 0, toTs = ""):
        url = 'https://min-api.cryptocompare.com/data/histohour?fsym='
        url += currency + '&tsym='
        url += baseCurrency + '&limit='
        url += str(limit) + '&aggregate=' + str(aggregate)
        url += toTs
        return self.query(url)["Data"]
        
    def histoDay(self, currency, baseCurrency = 'BTC', limit = 60, aggregate = 0, toTs = ""):
        url = 'https://min-api.cryptocompare.com/data/histoday?fsym='
        url += currency + '&tsym='
        url += baseCurrency + '&limit='
        url += str(limit) + '&aggregate=' + str(aggregate)
        url += toTs
        return self.query(url)["Data"]
