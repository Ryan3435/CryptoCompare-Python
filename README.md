CryptoCompare-Python

This is a wrapper for CryptoCompare's public API.

Full documentation can be found here: https://min-api.cryptocompare.com/
More information here: https://www.cryptocompare.com/api/#introduction

Functions currently supported:

price(self,currency,inTermsOf='BTC')
priceHistorical(self,currency,inTermsOf='BTC')
generateAvg(self,currency,inTermsOf='USD',markets='Coinbase,Kraken,Bitstamp,Bitfinex')
histoMinute(self, currency, baseCurrency = 'BTC', limit = 60, aggregate = 0, toTs = "")
histoHour(self, currency, baseCurrency = 'BTC', limit = 60, aggregate = 0, toTs = "")
histoDay(self, currency, baseCurrency = 'BTC', limit = 60, aggregate = 0, toTs = "")

I will try to finish the rest of the functions soon.
