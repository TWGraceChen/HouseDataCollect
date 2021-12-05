# -*- coding: utf-8 -*-
"""
@author: Hank
"""

import requests
from src import function as func
#import sys

def Extract(path):
    print("====airport====")
    url = " https://quality.data.gov.tw/dq_download_csv.php?nid=8093&md5_url=573e3aadae08c74d3735dff33fec2545"
    req = requests.get(url)
    url_content = req.content.decode('utf-8') #.encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    output = path+'/airport.csv'
    func.writetofile(output,url_content)




if __name__ == '__main__':
    Extract('./data')