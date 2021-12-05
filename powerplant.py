# -*- coding: utf-8 -*-
"""
@author: Hank
"""

import requests
from src import function as func
import sys

def Extract(path):
    print("====powerplant====")
    url = " https://data.taipower.com.tw/opendata/apply/file/d004001/001.csv"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/powerplant.csv'
    func.writetofile(output,url_content)




if __name__ == '__main__':
    Extract('./data')
