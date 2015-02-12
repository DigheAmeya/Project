import Quandl
#mydata = Quandl.get("WIKI/AAPL")
#mydata = Quandl.get("FRED/GDP")
#mydata = Quandl.get("OFDP/FUTURE_ESZ2014")
#mydata = Quandl.get("OFDP/FUTURE_ADH1987")
mydata = Quandl.get("YAHOO/ALMIL_PA")
#mydata = Quandl.get("GOOG")
print(mydata)
mydata.describe

