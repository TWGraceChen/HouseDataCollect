# -*- coding: utf-8 -*-
"""
@author: Hank
"""
import requests, zipfile, io
import pathlib
import os
import shutil


def Extract(path):
    print("====funeralcompany====")
    #建立暫存資料夾
    doc = path+"/funeralcompany"
    try:
        os.mkdir(doc)
        print("build File...")
    except OSError as e:
        print(e)
    else:
        print("File is already build")
        
    url = "https://data.gcis.nat.gov.tw/od/file?oid=6EEC675F-3972-47AE-B157-B92CA5749773"
    req = requests.get(url)
    
    z = zipfile.ZipFile(io.BytesIO(req.content))
    z.extractall(doc)
    
    file = str(list(pathlib.Path(doc).glob(r"*.csv"))[0])
    #print(doc+file)
    os.replace(file, path+"/funeralcompany.csv")
    
    #刪除暫存資料夾
    try:
        shutil.rmtree(doc)
    except OSError as e:
        print(e)
    else:
        print("finish")



if __name__ == '__main__':
    Extract('../data')