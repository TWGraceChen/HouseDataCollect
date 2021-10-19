
import requests
import csv
import json

alldata = []



url = "https://www.costco.com.tw/store-finder/search?q=%E8%87%BA%E7%81%A3"
response = requests.request("GET", url)

for row in json.loads(response.content)['data']:
  data = [row['displayName'],row['warehouseCode'],row['name'],row['url'],row['phone'],row['formattedDistance'],row['addressId'],row['line1'],row['line2'],row['town'],row['postalCode'],row['email'],row['latitude'],row['longitude'],row['storeContent'],row['openings']['星期日']['individual'],row['openings']['星期一']['individual'],row['openings']['星期二']['individual'],row['openings']['星期三']['individual'],row['openings']['星期四']['individual'],row['openings']['星期五']['individual'],row['openings']['星期六']['individual'],row['openings']['星期日']['individual']]
  alldata.append(data)

# write to file
with open('./data/costco.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(alldata)

    