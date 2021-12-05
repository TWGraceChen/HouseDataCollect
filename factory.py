# -*- coding: utf-8 -*-
"""
@author: Hank
"""

import requests
import sys
from src import function as func

def Extract(path):
    print("====factory====")
    url = "	https://quality.data.gov.tw/dq_download_csv.php?nid=37314&md5_url=05110a8ef17113a6af180fe033b7c14b"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    #open('factory.csv', 'w')
    output = path+'/factory.csv'
    func.writetofile(output,url_content)




if __name__ == '__main__':
    Extract('./data')