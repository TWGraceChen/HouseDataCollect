# -*- coding: utf-8 -*-


import requests
from src import function as func
import sys
from src import bo
import json

def Extract(path):
    print("====nightmarket====")
    url = "https://www.cto.moea.gov.tw/OD/%E5%90%84%E7%B8%A3%E5%B8%82%E5%A4%9C%E5%B8%82%E8%B3%87%E6%96%99.csv"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/nightmarket.csv'
    func.writetofile(output,url_content)



def Transform(file):
    # 序號,縣市,鄉鎮市區,夜市名稱,地址,營業時間,市集特色(500字以內簡介)
    data = []
    idx = 1
    raw = func.readcsv(file)
    raw = raw[1:]
    for r in raw:
        xy = func.transgeo(r[1]+r[2]+r[4],"./geo")
        data.append([idx]+r+[xy['city'],xy['town'],xy['address'],xy['area'],xy['code2'],xy['code1'],xy['codebase'],xy['code'],xy['desc'],xy['x'],xy['y'],func.towkt(xy['x'],xy['y'])])
        idx = idx + 1
    return data



if __name__ == '__main__':
    # Extract
    #Extract('./data')
    
    # Transform
    data = Transform('./data/nightmarket.csv')
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "nightmarket"
    bo.load(db,table,schema[table],data)