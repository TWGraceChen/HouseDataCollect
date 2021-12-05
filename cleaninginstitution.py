# -*- coding: utf-8 -*-
"""
@author: Hank
"""

import requests
from src import function as func
import sys

def Extract(path):
    print("====cleaninginstitution====")
    url = "https://storage.googleapis.com/opendata2.epa.gov.tw/data/wr_s_05/wr_s_05.csv"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/cleaninginstitution.csv'
    func.writetofile(output,url_content)




if __name__ == '__main__':
    Extract('./data')