# -*- coding: utf-8 -*-
"""
@author: Hank
"""

import requests
import sys
from src import function as func

def Extract(path):
    print("====fm_radioaddress====")
    url = " https://www.ncc.gov.tw/chinese/files/opendata/fm.csv"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/fm_radioaddress.csv'
    func.writetofile(output,url_content)




if __name__ == '__main__':
    Extract('./data')
