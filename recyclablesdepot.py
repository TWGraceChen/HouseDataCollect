# -*- coding: utf-8 -*-
"""
@author: Hank
"""

import requests
from src import function as func
import sys

def Extract(path):
    print("====recyclablesdepot====")
    url = " https://data.epa.gov.tw/api/v1/wr_p_45?format=csv&api_key=1d3d5ea9-ce0d-4667-9eda-a625bc5aa408"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/recyclablesdepot.csv'
    func.writetofile(output,url_content)




if __name__ == '__main__':
    Extract('./data')