import requests, zipfile, io
from os import replace
import json
from src import function as func
from src import bo


def Extract(path):
    print("====hospital====")
    url = "https://www.nhi.gov.tw/DL.aspx?sitessn=292&u=LzAwMS9VcGxvYWQvMjkyL3JlbGZpbGUvMC84NDY3L2hvc3Bic2Muemlw&n=aG9zcGJzYy56aXA%3d"
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(path)
    output = path+"/hospital.csv"
    replace(path+"/hospbsc.txt",output )
    print("save csv:" + output)


def Transform(file):
    # 分區別,醫事機構代碼,醫事機構名稱,機構地址,電話區域號碼 ,電話號碼,特約類別,型態別,醫事機構種類,終止合約或歇業日期,開業狀況
    raw = func.readcsv(file,encode='utf16')
    raw = raw[1:]
    data = [] 
    for r in raw:
        row = r[:9]
        if len(r[9]) == 8:
            close_date = r[9][:4]+"-"+r[9][4:6]+"-"+r[9][6:8]
        else:
            close_date = ""
        row.append(close_date)
        row.append(r[10])

        if len(r[3]) > 0:
            xy = func.transgeo(r[3],"./geo")
            row = row + [xy['city'],xy['town'],xy['address'],xy['area'],xy['code2'],xy['code1'],xy['codebase'],xy['code'],xy['desc'],xy['x'],xy['y']]
        else:
            row = row + [""] * 11
        data.append(row)
        
    return data


if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    # Transform
    data = Transform('./data/hospital.csv')

    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "hospital"
    bo.load(db,table,schema[table],data)    