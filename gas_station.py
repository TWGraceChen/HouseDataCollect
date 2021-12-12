# -*- coding: utf-8 -*-
"""
@author: Hank
"""

import requests
import sys
from src import function as func
from src import bo
import json

def Extract(path):
    print("====gas_station====")
    url = " https://www3.cpc.com.tw/opendata_d00/webservice/加油站服務資訊.csv"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/gas_station.csv'
    func.writetofile(output,url_content)


def Transform(file):
    raw = func.readcsv(file)
    raw = raw[1:]
    data = []
    idx = 1
    for r in raw:
        data.append([idx]+r+[func.towkt(r[23],r[24])])
        idx = idx + 1
    return data



if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    # Transform
    data = Transform('./data/gas_station.csv')
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "gas_station"
    bo.load(db,table,schema[table],data)