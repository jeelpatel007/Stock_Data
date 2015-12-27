__author__ = 'jeel'

# importing required modules for working with web-urls
from urllib import request

# This is a direct link to download the historical stock price of Google
goog_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=11&e=27&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv"

'''
Function 'download_stock_data' is the main function.
It begins with recording the response (data) from the URL.
Then the response is stored in a variable 'csv', which is later converted into string.
Each line in the csv file is then split into new line.
Later part creates a file 'goog.csv' and then populates it with the data we already collected.
'''
def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()
    
if __name__ == '__main__':
    download_stock_data(goog_url)
