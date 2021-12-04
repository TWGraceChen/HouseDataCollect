import requests
import json
import zipfile
import io
from src import function as func
from src import bo
import geopandas as gpd


def Extract(path):
    print("====最小統計區====")
    url = "https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=D6AA982D-9833-48EC-8CA1-1D3D13505AF1"
    r = requests.get(url)
    with open(path+"/shp/code0.rar","wb") as code:
        code.write(r.content)
    

    print("====一級發布區====")
    url = "https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=0DAB14B7-B637-417D-8721-BE89AD391176"
    r = requests.get(url)
    with open(path+"/shp/code1.rar","wb") as code:
        code.write(r.content)


    print("====二級發布區====")
    url = "https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=7E4430F1-2070-4663-907B-452A545CCC8B"
    r = requests.get(url)
    with open(path+"/shp/code2.rar","wb") as code:
        code.write(r.content)


    
    print("====村里發布區====")
    url = "https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=B8AF344F-B5C6-4642-AF46-1832054399CE"
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    dirname = path+"/shp/village"
    z.extractall(dirname)


def Transform(path):
    shapefile = gpd.read_file(path + '/code0/G97_TW_U0200_2015.shp')
    data0 = []
    for d in shapefile.iterrows():
        new_poly = func.polyztopoly(d[1][11])
        data0.append([d[1][1],d[1][2],d[1][3],d[1][4],d[1][5],d[1][6],d[1][7],d[1][0],d[1][8]]+func.TWDToGPS(d[1][9],d[1][10]) + [new_poly,new_poly])

    shapefile = gpd.read_file(path + '/code1/G97_TW_U0201_2015.shp')
    data1 = []
    for d in shapefile.iterrows():
        new_poly = func.polyztopoly(d[1][10])
        data1.append([d[1][0],d[1][1],d[1][2],d[1][3],d[1][4],d[1][5],d[1][6],d[1][7]]+func.TWDToGPS(d[1][8],d[1][9]) + [new_poly,new_poly])

    shapefile = gpd.read_file(path + '/code2/G97_TW_U0202_2015.shp')
    data2 = []
    for d in shapefile.iterrows():
        new_poly = func.polyztopoly(d[1][9])
        data2.append([d[1][0],d[1][1],d[1][2],d[1][3],d[1][4],d[1][5],d[1][6]]+func.TWDToGPS(d[1][7],d[1][8]) + [new_poly,new_poly])
    

    shapefile = gpd.read_file(path + '/village/VILLAGE_MOI_1101007.shp', encoding='utf-8')
    datavillage = []
    for d in shapefile.iterrows():
        poly = func.polytomultipoly(d[1][10])
        datavillage.append([d[1][0],d[1][1],d[1][2],d[1][3],d[1][4],d[1][5],d[1][6],d[1][7],d[1][8],d[1][9],poly,poly])
    

    return data0,data1,data2,datavillage

if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    # Transform
    data0,data1,data2,datavillage = Transform('./data/shp')
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "area_code0"
    bo.load(db,table,schema[table],data0,batch_size=100)    
    table = "area_code1"
    bo.load(db,table,schema[table],data1,batch_size=100)    
    table = "area_code2"
    bo.load(db,table,schema[table],data2,batch_size=100)    
    table = "area_village"
    bo.load(db,table,schema[table],datavillage,batch_size=100)  

    