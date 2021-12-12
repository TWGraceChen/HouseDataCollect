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
    print("====recyclablesdepot====")
    url = " https://data.epa.gov.tw/api/v1/wr_p_45?format=csv&api_key=1d3d5ea9-ce0d-4667-9eda-a625bc5aa408"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/recyclablesdepot.csv'
    func.writetofile(output,url_content)



def Transform(file):
    data = []
    idx = 1
    raw = func.readcsv(file)
    raw = raw[1:]
    for r in raw:
        xy = func.transgeo(r[2],"./geo")
        data.append([idx]+r+[xy['city'],xy['town'],xy['address'],xy['area'],xy['code2'],xy['code1'],xy['codebase'],xy['code'],xy['desc'],xy['x'],xy['y'],func.towkt(xy['x'],xy['y'])])
        idx = idx + 1
    return data



if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    # Transform
    data = Transform('./data/recyclablesdepot.csv')
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "recyclablesdepot"
    bo.load(db,table,schema[table],data)