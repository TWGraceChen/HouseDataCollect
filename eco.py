import requests
from requests.packages import urllib3
import json
from src import function as func
from src import bo

def Extract(path):
    print("====eco====")
    urllib3.disable_warnings()
    url = "https://apiservice.mol.gov.tw/OdService/download/A17030000J-000016-wWs"
    response = requests.request("GET", url, verify=False)
    content = response.content.decode('utf-8')
    output = path+'/eco.csv'  
    func.writetofile(output,content)  


def Transform(file):
    # 月別,經濟成長率,平均每人國民所得毛額（美元）,儲蓄率,失業率,產業結構（按各產業GDP比重）-農業,產業結構（按各產業GDP比重）-工業,產業結構（按各產業GDP比重）-服務業,產業結構（按各產業GDP比重）-服務業-金融中介業,產業結構（按各產業GDP比重）-服務業-保險業,產業結構（按各產業GDP比重）-服務業-證券期貨及其它金融業,躉售物價-指數,躉售物價-年增率,消費者物價-指數,消費者物價-年增率,基本工資（元）-月薪,基本工資（元）-時薪,工業及服務業平均月薪資（元）,製造業平均月薪資（元）,工業及服務業平均月工時（小時）
    raw = func.readcsv(file)
    raw = raw[1:]
    data = [] 
    for r in raw:
        row = []
        row.append(r[0].split("-")[0])
        row.append(r[0].split("-")[1])
        for col in r[1:]:
            row.append(col.replace("…","").replace(",","").replace("r","").replace(" ","").replace("p",""))

        data.append(row)
        
    return data




if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    # Transform
    data = Transform('./data/eco.csv')

    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "eco"
    bo.load(db,table,schema[table],data)    