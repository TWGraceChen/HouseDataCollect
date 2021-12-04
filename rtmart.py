import requests
from bs4 import BeautifulSoup
from src import function as func
from src import bo
import json

def Extract(path):
    print("====rtmart====")
    alldata = []
    url = "https://news.rt-mart.com.tw/main/%E5%88%86%E5%BA%97%E8%B3%87%E8%A8%8A-61"
    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text,features="lxml")


    for i in soup.find_all("div",{"class":"css-j4j7eh"}):

        try:
            name = i.find("p",{"class":"inner"}).text.replace("\n","")
            address = i.find("div",{"class":"caption"}).text.replace("地址：","").replace("\n","")
            alldata.append([name,address])
        except Exception as e:
            continue

    output = path+'/rtmart.csv'
    func.writetofile(output,alldata)

def Transform(file):
    raw = func.readcsv(file)
    data = []
    for r in raw:
        xy = func.transgeo(r[1],"./geo")
        row = r + [xy['city'],xy['town'],xy['address'],xy['area'],xy['code2'],xy['code1'],xy['codebase'],xy['code'],xy['desc'],xy['x'],xy['y'],func.towkt(xy['x'],xy['y'])]
      
        data.append(row)
    return data


if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    # Transform
    data = Transform('./data/rtmart.csv')

    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "rtmart"
    bo.load(db,table,schema[table],data)    