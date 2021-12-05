
import requests
import json
from src import function as func
from src import bo

def Extract(path):
  print("====costco====")
  alldata = []
  url = "https://www.costco.com.tw/store-finder/search?q=%E8%87%BA%E7%81%A3"
  response = requests.request("GET", url)

  for row in json.loads(response.content)['data']:
    data = [row['displayName'],row['warehouseCode'],row['name'],row['url'],row['phone'],row['formattedDistance'],row['addressId'],row['line1'],row['line2'],row['town'],row['postalCode'],row['email'],row['latitude'],row['longitude'],row['storeContent'],row['openings']['星期日']['individual'],row['openings']['星期一']['individual'],row['openings']['星期二']['individual'],row['openings']['星期三']['individual'],row['openings']['星期四']['individual'],row['openings']['星期五']['individual'],row['openings']['星期六']['individual']]
    alldata.append(data)


  output = path+'/costco.csv'
  func.writetofile(output,alldata)




def Transform(file):
    raw = func.readcsv(file)
    data = []
    idx = 1
    for r in raw:
      data.append([idx]+r+[func.towkt(r[13],r[12])])
      idx = idx +1
    return data

if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    ## Transform
    data = Transform('./data/costco.csv')

    ## Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "costco"
    bo.load(db,table,schema[table],data)    