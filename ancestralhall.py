"""
@author: Hank
"""
import requests
import xml.etree.ElementTree as ET
from src import function as func
from src import bo
import json

def Extract(path):
    print("====ancestralhall====")
    alldata_base = []
    column = ["宗祠名稱", "行政區", "地址", "電話", "負責人", "WGS84X", "WGS84Y"]
    alldata_base.append(column) #csv欄位
    url = "https://religion.moi.gov.tw/Report/Ancestral.xml"
    req = requests.get(url)
    xml = ET.fromstring(req.content)
    #print(xml)
    for data in xml.findall("OpenData_6"):
        row = []
        for i in range(len(column)):
            if data.find(column[i]) != None: #判斷是否不為空值
                row.append(data.find(column[i]).text) #不為空值填入資料
            else:
                row.append("") #空值填入null

        alldata_base.append(row) #完成一筆資料寫到alldata_base
    
    output = path+'/ancestralhall.csv'
    func.writetofile(output,alldata_base)

def Transform(file):
    # 宗祠名稱,行政區,地址,電話,負責人,WGS84X,WGS84Y
    raw = func.readcsv(file)
    raw = raw[1:]
    data = [] 
    idx = 1
    for r in raw:
        data.append([idx]+r+[func.towkt(r[5],r[6])])
        idx = idx +1
        
    return data

if __name__ == '__main__':
    # Extract
    #Extract('./data')
    
    # Transform
    data = Transform('./data/ancestralhall.csv')

    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "ancestralhall"
    bo.load(db,table,schema[table],data)  