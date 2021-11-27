import requests
import xml.etree.ElementTree as ET
from src import function as func
from src import bo
import json

def Extract(path):
    print("====shopseven====")
    alldata = []
    url = "https://emap.pcsc.com.tw/EMapSDK.aspx"

    citylist = {'01':'台北市','02':'基隆市','03':'新北市','04':'桃園市','05':'新竹市','06':'新竹縣','07':'苗栗縣','08':'台中市','10':'彰化縣','11':'南投縣','12':'雲林縣','13':'嘉義市','14':'嘉義縣','15':'台南市','17':'高雄市','19':'屏東縣','20':'宜蘭縣','21':'花蓮縣','22':'台東縣','23':'澎湖縣','24':'連江縣','25':'金門縣'}
    for cityid in citylist:
        city = citylist[cityid]
        # get town in city
        payload={'commandid': 'GetTown','cityid': cityid}
        response = requests.request("POST", url,data=payload)
        townxml = ET.fromstring(response.text)
        for x in townxml.findall('GeoPosition'):
            towmid = x.find("TownID").text
            townname = x.find("TownName").text
            townx = x.find("X").text
            towny = x.find("Y").text

            # get shop in town
            payload={'commandid': 'SearchStore','city': city,'town': townname}
            response = requests.request("POST", url, data=payload)
            shopxml = ET.fromstring(response.text)
            for y in shopxml.findall('GeoPosition'):
                poiid = y.find("POIID").text.strip()
                poiname = y.find("POIName").text
                poix = y.find("X").text
                poiy = y.find("Y").text
                poitelno = y.find("Telno").text.strip()
                poifaxno = y.find("FaxNo").text.strip()
                poiaddress = y.find("Address").text
                poiimg = y.find("StoreImageTitle").text
                data = [cityid,city,towmid,townname,townx,towny,poiid,poiname,poix,poiy,poitelno,poifaxno,poiaddress,poiimg]
                alldata.append(data)
            print(city+townname)

    output = path+'/shopseven.csv'
    func.writetofile(output,alldata)

def Transform(file):
    data = func.readcsv(file)
    for i in range(len(data)):
        data[i][4] = float(data[i][4])/1000000
        data[i][5] = float(data[i][5])/1000000
        data[i][8] = float(data[i][8])/1000000
        data[i][9] = float(data[i][9])/1000000

    return data


if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    # Transform
    data = Transform('./data/shopseven.csv')

    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "shopseven"
    bo.load(db,table,schema[table],data)    
