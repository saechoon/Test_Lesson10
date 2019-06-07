class Stocks():
    def __init__(self, symbol, date, openValue, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.openValue = openValue
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        #self.stockCloseList=[]
        #self.stockopenValueList=[]
        #self.stockHighList=[]
        #self.stockLowList=[]
        self.stockVolumeList=[]
        self.stockDate=[]
        self.stockName=(symbol)
       
     
    def addVolume(self, volume, date):
        """Add information to the class"""
        self.stockVolumeList.append(volume)
        self.stockDate.append(date)
