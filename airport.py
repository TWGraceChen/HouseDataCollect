# -*- coding: utf-8 -*-
"""
@author: Hank
"""

import requests
from src import function as func
from src import bo
import json
#import sys

def Extract(path):
    print("====airport====")
    url = "https://quality.data.gov.tw/dq_download_csv.php?nid=8093&md5_url=573e3aadae08c74d3735dff33fec2545"
    req = requests.get(url)
    url_content = req.content.decode('utf-8') #.encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/airport.csv'
    func.writetofile(output,url_content)


def Transform(file):
    raw = func.readcsv(file)
    raw = raw[1:]
    data = []
    idx = 1
    last = []
    for r in raw:
        if r[0] == "":
            r[0] = last[0]
            r[2] = last[2]
        xy = func.transgeo(r[2].replace(' ',''),"./geo")
        data.append([idx]+r+[xy['city'],xy['town'],xy['address'],xy['area'],xy['code2'],xy['code1'],xy['codebase'],xy['code'],xy['desc'],xy['x'],xy['y'],func.towkt(xy['x'],xy['y'])])
        last = r
        idx = idx + 1
    return data

if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    # Transform
    data = Transform('./data/airport.csv')
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "airport"
    bo.load(db,table,schema[table],data)