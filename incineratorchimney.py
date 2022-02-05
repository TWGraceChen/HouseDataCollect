"""
@author: Hank
"""
import requests, zipfile, io
import os 
import pathlib #need pip install
import geopandas #need pip install
import shutil #need pip install
from src import function as func
from src import bo
import json


def Extract(path):
    print("====incineratorchimney====")
    #建立暫存資料夾
    doc = path+"/incineratorchimney"
    try:
        os.mkdir(doc)
        print("build File...")
    except OSError as e:
        print(e)
    else:
        print("File is already build")
    
    print("Request...")
    url = "https://geoser.epa.gov.tw/portal/sharing/rest/content/items/6dabf476a68b4e01affc11f6a9f323b5/data"
    r = requests.get(url)
  
    print("Unzip...")
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(doc)
    
    print("Rename...")
    extlist = [r"*.shx",r"*.shp",r"*.dbf"]
    renamelist =[doc+"/incineratorchimney.shx",doc+"/incineratorchimney.shp",doc+"/incineratorchimney.dbf"]
    fileDir = doc
    
    for i in range(len(extlist)):
        file = str(list(pathlib.Path(fileDir).glob(extlist[i]))[0])
        os.rename(file,renamelist[i])
        print(renamelist[i])
  
    print("Write into csv...") 
    data = geopandas.read_file(doc+"/incineratorchimney.shp", encoding='cp950') #讀取磁碟上的向量檔案
    data.to_csv(path+"/incineratorchimney.csv") #寫成csv
    
    #刪除暫存資料夾
    try:
        shutil.rmtree(doc)
    except OSError as e:
        print(e)
    else:
        print("finish")

def Transform(file):
    raw = func.readcsv(file)
    raw = raw[1:]
    data = []
    idx = 1
    for r in raw:
        data.append([idx]+r)
        idx = idx + 1
    return data   
    

if __name__ == '__main__':
    # Extract
    #Extract('./data')
    
    # Transform
    data = Transform('./data/incineratorchimney.csv')
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "incineratorchimney"
    bo.load(db,table,schema[table],data)