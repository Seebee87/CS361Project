"""*******************************************************************************************
Title: Web Scraping 1: Scraping Table Data
Author: Kiprono Elijah Koech
Date: 11/11/21
Located: https://towardsdatascience.com/web-scraping-scraping-table-data-1665b6b2271c

I used this as a guide to get my web scraping working on a table for the S&P 500. I tried for 
many, many hours to get a scrapy spider to work with flask but it just seems impossible, so went
for a more simplified version. This code returns the last 10 years of the S&P 500 and associated
data as a JSON file when a request is called to the server. 
*******************************************************************************************"""

from flask import Flask, render_template
from bs4 import BeautifulSoup
import json
import requests
import re

from requests.api import head

#GET request to path
html_data = requests.get('https://www.macrotrends.net/2526/sp-500-historical-annual-returns').text

#get html data from site
soup = BeautifulSoup(html_data, 'lxml')

#find all 'tables' css class on the page (There are 3)
all_tables = soup.find_all("table", attrs={"class": "table"})
#select the first table, which is the one we want
stock_table = all_tables[0]
#put all of the rows into a variable row_data
row_data = stock_table.find_all("tr")
#the first row [0] is just the title, [1] is the headers
header = row_data[1]
#data_rows grabs the 10 years of what we need
data_rows = row_data[2:12]

#for loop to parse the data in the header rows
headings = []
for item in header.find_all("th"):
    #strip unwanted markup text
    item = (item.text).rstrip('\n')
    headings.append(item)

#for loop to parse the data in the body of the table
ten_rows = []
for rows in range(len(data_rows)):
    row = []
    for cell_data in data_rows[rows].find_all("td"):
        #strip unwanted markup text
        data = re.sub("(\xa0)|(\n)|,","",cell_data.text)
        row.append(data)
    ten_rows.append(row)

#put data into single list
ten_year_data = []
ten_year_data.append(headings)
ten_year_data.append(ten_rows)

#convert list to json
jsonString = json.dumps(ten_year_data)


#set up flask server
app = Flask(__name__)

@app.route("/")
def get_history():
    #return jsonString to any GET requests
    return(jsonString)

app.run(port=4400)



