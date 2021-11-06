import requests
import os


url = "	https://www.cbc.gov.tw/public/data/OpenData/A13Rate.csv"
content = requests.get(url).content
csv_file = open('./data/rate.csv', 'wb')
csv_file.write(content)
csv_file.close()

print("====Finish====")
