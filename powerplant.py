# -*- coding: utf-8 -*-
"""
@author: Hank
"""

import requests
from src import function as func
import sys
from src import bo
import json

def Extract(path):
    print("====nuclear_powerplant====")
    url = " https://data.taipower.com.tw/opendata/apply/file/d004001/001.csv"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/powerplant.csv'
    func.writetofile(output,url_content)


def Transform(file):
    #電廠名稱,地址,連絡電話,傳真電話,機組名稱,商轉日期,裝置容量(瓩),燃料種類
    data = []
    idx = 1
    raw = func.readcsv(file)
    raw = raw[1:]
    for r in raw:
        address = r[1][5:].replace(' ','')
        xy = func.transgeo(address,"./geo")
        try:
            y = int(r[5].split(".")[0]) + 1911
            m = r[5].split(".")[1]
            d = r[5].split(".")[2]
            dt = "{}-{}-{}".format(y,m,d)
        except:
            dt = ""
        data.append([idx]+r[:5]+[dt,r[6].replace(',',''),r[7]]+[xy['city'],xy['town'],xy['address'],xy['area'],xy['code2'],xy['code1'],xy['codebase'],xy['code'],xy['desc'],xy['x'],xy['y'],func.towkt(xy['x'],xy['y'])])
        idx = idx + 1
    return data


if __name__ == '__main__':
    # Extract
    #Extract('./data')
    
    # Transform
    data = Transform('./data/powerplant.csv')
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "powerplant"
    bo.load(db,table,schema[table],data)