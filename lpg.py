# -*- coding: utf-8 -*-


import requests
import sys
from src import function as func
from src import bo
import json

def Extract(path):
    print("====lpg====")
    url = " https://www.moeaboe.gov.tw/ECW/populace/opendata/wHandOpenData_File.ashx?set_id=106"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/lpg.csv'
    func.writetofile(output,url_content)


def Transform(file):
    raw = func.readcsv(file)
    raw = raw[1:]
    data = []
    idx = 1
    
    for r in raw:
        xy = func.transgeo(r[3]+r[4]+r[5],"./geo")
        data.append([idx]+r+[xy['city'],xy['town'],xy['address'],xy['area'],xy['code2'],xy['code1'],xy['codebase'],xy['code'],xy['desc'],xy['x'],xy['y'],func.towkt(xy['x'],xy['y'])])
        idx = idx + 1
    
    return data



if __name__ == '__main__':
    # Extract
    #Extract('./data')
    
    # Transform
    data = Transform('./data/lpg.csv')
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "lpg"
    bo.load(db,table,schema[table],data)