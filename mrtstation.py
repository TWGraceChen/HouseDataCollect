import requests
import json
from src import function as func
from src import bo

def Extract(path):
    print("====mrtstation====")
    url = "https://data.taipei/api/getDatasetInfo/downloadResource?id=cfa4778c-62c1-497b-b704-756231de348b&rid=42694bb8-fc9d-4d82-af7a-0ad6f4c9ad57"
    req = requests.get(url)
    url_content = req.content.decode('big5')
    
    output = path+"/mrtstation.csv"
    func.writetofile(output,url_content)

def Transform(file):
    # 項次,出入口名稱,出入口編號,經度,緯度
    data = func.readcsv(file)
    data = data[1:]
    
    return data


if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    # Transform
    data = Transform('./data/mrtstation.csv')

    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "mrtstation"
    bo.load(db,table,schema[table],data) 