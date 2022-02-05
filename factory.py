# -*- coding: utf-8 -*-
"""
@author: Hank
"""

import requests
import sys
import json
from src import function as func
from src import bo

def Extract(path):
    print("====factory====")
    url = "	https://quality.data.gov.tw/dq_download_csv.php?nid=37314&md5_url=05110a8ef17113a6af180fe033b7c14b"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/factory.csv'
    func.writetofile(output,url_content)


def Transform(file):
    raw = func.readcsv(file)
    raw = raw[1:]
    data = []
    idx = 1
    for r in raw:
        data.append([idx]+r)
        idx = idx +1
    return data

if __name__ == '__main__':
    # Extract
    #Extract('./data')
    
    # Transform
    data = Transform('./data/factory.csv')
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "factory"
    bo.load(db,table,schema[table],data)