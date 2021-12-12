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
    print("====am_radio====")
    url = " https://www.ncc.gov.tw/chinese/files/opendata/am.csv"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/am_radio.csv'
    func.writetofile(output,url_content)

    print("====fm_radio====")
    url = " https://www.ncc.gov.tw/chinese/files/opendata/fm.csv"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/fm_radio.csv'
    func.writetofile(output,url_content)


def Transform(files):
    data = []
    idx = 1
    for file in files:
        raw = func.readcsv(file)
        raw = raw[1:]
        for r in raw:
            data.append([idx]+r+[func.towkt(r[3],r[4])])
            idx = idx + 1
    return data

if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    # Transform
    data = Transform(['./data/am_radio.csv','./data/fm_radio.csv'])
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "radio"
    bo.load(db,table,schema[table],data)