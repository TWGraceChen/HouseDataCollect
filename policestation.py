import requests
import zipfile
import io,os
import shutil
import json
from src import function as func
from src import bo


def Extract(path):
    print("====policestation====")
    url = "	https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=EE144E5A-39DE-4A20-9654-B295EB9F9F19"

    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))

    dirname = path+"/policestation/"
    z.extractall(dirname)
    
    output = path+"/policestation.csv"
    for filename in os.listdir(dirname):
        if "Address" in filename:
            shutil.move(dirname+filename, output)
            print("save csv:" + output)
    shutil.rmtree(dirname)

def Transform(file):
    # 中文單位名稱,英文單位名稱,郵遞區號,地址,電話,POINT_X,POINT_Y
    raw = func.readcsv(file)
    raw = raw[1:]
    data = [] 
    for r in raw:
        data.append(r+func.TWDToGPS(float(r[5]),float(r[6])))
    
    return data


if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    # Transform
    data = Transform('./data/policestation.csv')
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "policestation"
    bo.load(db,table,schema[table],data)    

    