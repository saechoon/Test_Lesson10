"""
Description: The program creates a plot of stock volumes by dates.

This assignment inputs a data file, AllStocks.json, and outputs the values to a pygal simple chart.

Author: Sammy Chung

Last revision: 6/7/2019
"""
import stocks
import json
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime


filePath =  r"G:\To do\Classes\PythonICT4370\Lesson08\AllStocks.json"
try:
        with open(filePath) as f:
            dataSet = json.load(f)

        stockDictionary = {}
        ##fig, ax = plt.subplots(figsize=(8,5))
        ##fig.subplots_adjust(bottom=0.2)
        for invest in dataSet:
                if invest['Symbol'] not in stockDictionary:
                        newStock = stocks.Stocks(invest['Symbol'], invest['Date'], invest['Open'], invest['High'], invest['Low'], invest['Close'], invest['Volume'])
                        print (invest['Symbol'] + " added")
                        stockDictionary[invest['Symbol']] = {'Symbol': newStock}
                stockDictionary[invest['Symbol']]['Symbol'].addVolume(invest['Volume'],datetime.strptime(invest['Date'], '%d-%b-%y'))

        for invest in stockDictionary:
                weights2 = stockDictionary[invest]['Symbol'].stockVolumeList
                dates = matplotlib.dates.date2num(stockDictionary[invest]['Symbol'].stockDate)
                name = stockDictionary[invest]['Symbol'].stockName
                plt.plot_date(dates, weights2, linestyle='solid', marker='None', label = name)

        plt.legend(loc='best')
        plt.rc('font', size=10)
        plt.savefig('simplePlot.png')
except IndexError:
    print('There was an IndexError. Index is out of range.')
except NameError:
    print('There was a NameError.Local or global name is not found.')	
