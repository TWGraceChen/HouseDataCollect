# -*- coding: utf-8 -*-
"""
@author: Hank
"""

import requests
from src import function as func
import sys

def Extract(path):
    print("====am_radioaddress====")
    url = " https://www.ncc.gov.tw/chinese/files/opendata/am.csv"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/am_radioaddress.csv'
    func.writetofile(output,url_content)




if __name__ == '__main__':
    Extract('./data')
