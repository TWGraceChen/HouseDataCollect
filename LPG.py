# -*- coding: utf-8 -*-
"""
@author: Hank
"""

import requests
from src import function as func
import sys

def Extract(path):
    print("====LPG====")
    url = " https://www3.cpc.com.tw/opendata_d00/webservice/加油站服務資訊.csv"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    #open('LPG.csv','w', newline='')
    output = path+'/LPG.csv'
    func.writetofile(output,url_content)




if __name__ == '__main__':
    Extract('./data')
