import requests
import json
import sqlite3

# create database if it doesn't exist
dbc = sqlite3.connect("bitcoinanalysis.db")
cursor = dbc.cursor()

# create table if it doesn't exist
sql = "create table if not exists prices (month text, high real, low real)"
cursor.execute(sql)
dbc.commit()

# call the api to get monthly time series data
url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol=BTC&market=GBP&apikey=3TTLQ75V9FJXGEAQ"
res = requests.get(url)
content = res.content.decode("utf-8")

# turn the response into json
jsoncontent = json.loads(content)

# examine the json
for month in jsoncontent["Time Series (Digital Currency Monthly)"]:
    # get high and low prices
    highvalue = float(jsoncontent["Time Series (Digital Currency Monthly)"][month]["2a. high (GBP)"])
    lowvalue = float(jsoncontent["Time Series (Digital Currency Monthly)"][month]["3a. low (GBP)"])
    print(f"{month} : {highvalue} : {lowvalue}")

    # insert into the database
    sql = f"insert into prices values('{month}', {highvalue}, {lowvalue})"
    print(sql)
    cursor.execute(sql)
    dbc.commit()

print("-----------------------------------------------------")

# check the data in the database
sql = "select * from prices"
cursor.execute(sql)
data = cursor.fetchall()
print(data)

print("-----------------------------------------------------")

sql = "select month, high from prices where high = (select max(high) from prices)"
cursor.execute(sql)
data = cursor.fetchall()
print(data)

sql = "select month, low from prices where low = (select min(low) from prices)"
cursor.execute(sql)
data = cursor.fetchall()
print(data)

#3TTLQ75V9FJXGEAQ
