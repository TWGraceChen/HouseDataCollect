import requests
from src import function as func
from src import bo
import json

def Extract(path):
    print("====rate====")
    url = "	https://www.cbc.gov.tw/public/data/OpenData/A13Rate.csv"
    content = requests.get(url).content.decode('utf-8')
    output = path+'/rate.csv'
    func.writetofile(output,content)

def Transform(file):
    raw = func.readcsv(file)
    raw = raw[1:]
    data = []
    for r in raw:
        row = [r[0]]
        year = int(r[1][:3]) + 1911
        month = r[1][3:]
        row.append(year)
        row.append(month)
        row = row + r[2:]
        data.append(row)
    return data



if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    # Transform
    data = Transform('./data/rate.csv')

    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "rate"
    bo.load(db,table,schema[table],data)    

    
