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
    url = "https://data.taipower.com.tw/opendata/apply/file/d056001/%E5%8F%B0%E7%81%A3%E9%9B%BB%E5%8A%9B%E5%85%AC%E5%8F%B8_%E6%A0%B8%E8%83%BD%E7%99%BC%E9%9B%BB%E5%BB%A0%E4%BD%8D%E7%BD%AE%E5%8F%8A%E6%A9%9F%E7%B5%84%E8%A8%AD%E5%82%99.csv"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/nuclear_powerplant.csv'
    func.writetofile(output,url_content)


def Transform(file):
    # 電廠名稱,機組名稱,地址,連絡電話,傳真電話,商轉日期,"裝置容量(MWe)"
    data = []
    idx = 1
    raw = func.readcsv(file)
    raw = raw[1:]
    for r in raw:
        address = r[2].replace(' ','')
        xy = func.transgeo(address,"./geo")
        r[5] = r[5].replace(".","-")
        r[6] = r[6].replace(',','')
        data.append([idx]+r+[xy['city'],xy['town'],xy['address'],xy['area'],xy['code2'],xy['code1'],xy['codebase'],xy['code'],xy['desc'],xy['x'],xy['y'],func.towkt(xy['x'],xy['y'])])
        idx = idx + 1
    return data


if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    # Transform
    data = Transform('./data/nuclear_powerplant.csv')
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "nuclear_powerplant"
    bo.load(db,table,schema[table],data)