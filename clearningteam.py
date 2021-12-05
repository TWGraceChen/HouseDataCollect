# -*- coding: utf-8 -*-
"""
@author: Hank
"""

import requests
import function as func
import sys

def Extract(path):
    print("====cleaningteam====")
    url = "https://data.epa.gov.tw/api/v1/wr_s_04?format=csv&api_key=1d3d5ea9-ce0d-4667-9eda-a625bc5aa408"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/cleaningteam.csv'
    func.writetofile(output,url_content)




if __name__ == '__main__':
    Extract('../data')