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
    print("====incineratorarea====")
    #建立暫存資料夾
    doc = path+"/incineratorarea"
    try:
        os.mkdir(doc)
        print("build File...")
    except OSError as e:
        print(e)
    else:
        print("File is already build")
    
    print("Request...")
    url = "https://geoser.epa.gov.tw/portal/sharing/rest/content/items/335a25279be644c38832a5c48c18643b/data"
    r = requests.get(url)
  
    print("Unzip...")
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(doc)
    
    print("Rename...")
    extlist = [r"*.shx",r"*.shp",r"*.dbf"]
    renamelist =[doc+"/incineratorarea.shx",doc+"/incineratorarea.shp",doc+"/incineratorarea.dbf"]
    fileDir = doc
    
    for i in range(len(extlist)):
        file = str(list(pathlib.Path(fileDir).glob(extlist[i]))[0])
        os.rename(file,renamelist[i])
        print(renamelist[i])
  
    print("Write into csv...") 
    data = geopandas.read_file(doc+"/incineratorarea.shx") #讀取磁碟上的向量檔案
    data.to_csv(path+"/incineratorarea.csv") #寫成csv
    
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
        xy = func.transgeo(r[3],"./geo")
        data.append([idx]+r+[xy['city'],xy['town'],xy['address'],xy['area'],xy['code2'],xy['code1'],xy['codebase'],xy['code'],xy['desc'],xy['x'],xy['y'],func.towkt(xy['x'],xy['y'])])
        idx = idx + 1
    return data    

if __name__ == '__main__':
    # Extract
    #Extract('./data')
    
    # Transform
    data = Transform('./data/incineratorarea.csv')
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "incineratorarea"
    bo.load(db,table,schema[table],data)