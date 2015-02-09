import Quandl
#mydata = Quandl.get("WIKI/AAPL")
mydata = Quandl.get("FRED/GDP")
print(mydata)
mydata.describe

