import requests
from src import function as func
from src import bo
import json

def Extract(path):
    print("====pharmarcy====")
    url = "	https://data.nhi.gov.tw/DataSets/DataSetResource.ashx?rId=A21030000I-D21005-001"
    req = requests.get(url)
    url_content = req.content.decode('utf-8')
    output = path+'/pharmarcy.csv'
    func.writetofile(output,url_content)


def Transform(file):
    # 醫事機構代碼,醫事機構名稱,醫事機構種類,電話,地址,分區業務組,特約類別,服務項目,診療科別,終止合約或歇業日期,固定看診時段,備註,縣市別代碼
    raw = func.readcsv(file)
    raw = raw[1:]
    data = [] 
    for r in raw:
        row = r[:9]
        if len(r[9]) == 8:
            close_date = r[9][:4]+"-"+r[9][4:6]+"-"+r[9][6:8]
        else:
            close_date = ""
        row.append(close_date)
        row = row + r[10:]

        if len(r[4]) > 0:
            xy = func.transgeo(r[4],"./geo")
            row = row + [xy['city'],xy['town'],xy['address'],xy['area'],xy['code2'],xy['code1'],xy['codebase'],xy['code'],xy['desc'],xy['x'],xy['y'],func.towkt(xy['x'],xy['y'])]
        else:
            row = row + [""] * 12
        data.append(row)
        
    return data



if __name__ == '__main__':
    # Extract
    #Extract('./data')
    
    # Transform
    data = Transform('./data/pharmarcy.csv')

    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "pharmarcy"
    bo.load(db,table,schema[table],data)    