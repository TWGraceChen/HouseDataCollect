# -*- coding: utf-8 -*-
"""
@author: Hank
"""
import requests, zipfile, io
import pathlib
import os
import shutil
import json
from src import function as func
from src import bo

def Extract(path):
    print("====funeralbussiness====")
    #建立暫存資料夾
    doc = path+"/funeralbussiness"
    try:
        os.mkdir(doc)
        print("build File...")
    except OSError as e:
        print(e)
    else:
        print("File is already build")
        
    url = "https://data.gcis.nat.gov.tw/od/file?oid=C855E073-2659-4A3C-9086-9B93600A894C"
    req = requests.get(url)
    
    z = zipfile.ZipFile(io.BytesIO(req.content))
    z.extractall(doc)
    
    file = str(list(pathlib.Path(doc).glob(r"*.csv"))[0])
    #print(doc+file)
    os.replace(file, path+"/funeralbussiness.csv")
    
    #刪除暫存資料夾
    try:
        shutil.rmtree(doc)
    except OSError as e:
        print(e)
    else:
        print("finish")



if __name__ == '__main__':
    # Extract
    Extract('./data')

    ## Transform
    #data = Transform('./data/funeralbussiness.csv')
    #
    ## Load
    #db = bo.conn("127.0.0.1",13303,"house")
    #with open("schema.json") as f:
    #    schema = json.load(f)
    #table = "funeralbussiness"
    #bo.load(db,table,schema[table],data)