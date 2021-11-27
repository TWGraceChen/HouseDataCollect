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
    return func.readcsv(file)[1:]


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

