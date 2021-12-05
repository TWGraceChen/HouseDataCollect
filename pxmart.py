
import requests
import json
from src import function as func
from src import bo

def Extract(path):
    print("====pxmart====")
    alldata = []
    url = "https://www.pxmart.com.tw/Api/api/Common/GetArea2"

    # get city list
    payload = "{\"city\":\"\",\"area\":\"\",\"type\":1,\"exclusiveId\":0}"
    headers = {'content-type': 'application/json;charset=UTF-8'}
    rescitylist = requests.request("POST", url, headers=headers, data=payload)
    for city in json.loads(rescitylist.content)['data']:
        cityname = city['key']
        cityvalue = city['value']
        # get town list
        payloadtown = "{\"city\":\""+cityvalue+"\",\"area\":\"\",\"type\":1,\"exclusiveId\":0}"
        restownlist = requests.request("POST", url, headers=headers, data=payloadtown.encode('utf-8'))
        for town in json.loads(restownlist.content)['data']:
            townname = town['key']
            townvalue = town['value']
            print(cityname+townname)
            urldetail = "https://www.pxmart.com.tw/Api/api/Shop/api/Shop/WEBGetShopList"
            payloadshop = "{\"city\":\""+cityvalue+"\",\"area\":\""+townvalue+"\",\"street\":\"\",\"name\":\"\",\"serviceProject\":[]}"
            responseshop = requests.request("POST", urldetail, headers=headers, data=payloadshop.encode('utf-8'))
            for shop in json.loads(responseshop.content)['data']:
                id = shop['id']
                name = shop['name']
                description = shop['description']
                startDate = shop['startDate']
                endDate = shop['endDate']
                phone = shop['phone']
                address = shop['address']
                longitude = shop['longitude']
                latitude = shop['latitude']
                cornerMark = shop['cornerMark']
                service = ",".join(shop['serviceProject'])
                data = [cityname,townname,id,name,description,startDate,endDate,phone,address,longitude,latitude,cornerMark,service]
                alldata.append(data)

    output = path+'/pxmart.csv'
    func.writetofile(output,alldata)

def Transform(file):
    raw = func.readcsv(file)
    data = []
    idx = 1
    for r in raw:
      data.append([idx]+r+[func.towkt(r[9],r[10])])
      idx = idx +1
    return data


if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    # Transform
    data = Transform('./data/pxmart.csv')
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "pxmart"
    bo.load(db,table,schema[table],data)    

    