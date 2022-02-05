"""
@author: Hank
"""
import requests
import csv
import xml.etree.ElementTree as ET
from src import function as func
from src import bo
import json

def Extract(path):
    print("====temple====")
    alldata_base = []
    column = ["編號","寺廟名稱", "主祀神祇", "行政區", "地址", "教別", "建別", "組織型態", "電話", "負責人", "WGS84X", "WGS84Y"]
    alldata_base.append(column) #csv欄位
    url = "https://religion.moi.gov.tw/Report/temple.xml"
    req = requests.get(url)
    xml = ET.fromstring(req.content)

    for data in xml.findall("OpenData_3"):
        row = []
        for i in range(len(column)):
            if data.find(column[i]) != None:
                row.append(data.find(column[i]).text)
            else:
                row.append("")
        alldata_base.append(row)
    output = path+'/temple.csv'
    func.writetofile(output,alldata_base)


def Transform(file):
    # 編號,寺廟名稱,主祀神祇,行政區,地址,教別,建別,組織型態,電話,負責人,WGS84X,WGS84Y
    raw = func.readcsv(file)
    raw = raw[1:]
    data = [] 
    idx = 1
    for r in raw:
        data.append([idx]+r+[func.towkt(r[10],r[11])])
        idx = idx +1
        
    return data

if __name__ == '__main__':
    # Extract
    #Extract('./data')
    
    # Transform
    data = Transform('./data/temple.csv')

    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "temple"
    bo.load(db,table,schema[table],data)  