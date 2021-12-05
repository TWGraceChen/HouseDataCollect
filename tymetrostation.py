import requests
from src import function as func
from src import bo
import json

def Extract(path):
    print("====tymetrostation====")
    url = "https://www.rb.gov.tw/public/files/artsinfo/1607418282-m0.csv"
    req = requests.get(url) 
    url_content = req.content.decode('utf-8')

    output = path+'/tymetrostation.csv'
    func.writetofile(output,url_content)

def Transform(file):
    raw = func.readcsv(file)
    raw = raw[1:]
    data = []
    idx = 1
    for r in raw:
      data.append([idx]+r+[func.towkt(r[2],r[1])])
      idx = idx +1
    return data


if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    # Transform
    data = Transform('./data/tymetrostation.csv')

    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "tymetrostation"
    bo.load(db,table,schema[table],data)    

