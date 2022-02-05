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
    print("====wastewater====")
    #建立暫存資料夾
    doc = path+"/wastewater"
    try:
        os.mkdir(doc)
        print("build File...")
    except OSError as e:
        print(e)
    else:
        print("File is already build")
    
    print("Request...")
    url = "https://geoser.epa.gov.tw/portal/sharing/rest/content/items/c7ff4242afd249bd9ddd710eba1e3c9f/data"
    r = requests.get(url)
  
    print("Unzip...")
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(doc)
    
    print("Rename...")
    extlist = [r"*.shx",r"*.shp",r"*.dbf"]
    renamelist =[doc+"/wastewater.shx",doc+"/wastewater.shp",doc+"/wastewater.dbf"]
    fileDir = doc
    
    for i in range(len(extlist)):
        file = str(list(pathlib.Path(fileDir).glob(extlist[i]))[0])
        os.rename(file,renamelist[i])
        print(renamelist[i])
  
    print("Write into csv...") 
    data = geopandas.read_file(doc+"/wastewater.shx") #讀取磁碟上的向量檔案
    data.to_csv(path+"/wastewater.csv") #寫成csv
    
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
        n = func.TWDToGPS(float(r[7]),float(r[8]))
        r[7] = n[1]
        r[8] = n[0]
        r[10] = func.towkt(r[7],r[8])
        data.append([idx]+r)
        idx = idx + 1
    return data   
    
if __name__ == '__main__':
    # Extract
    #Extract('./data')
    
    # Transform
    data = Transform('./data/wastewater.csv')
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "wastewater"
    bo.load(db,table,schema[table],data)