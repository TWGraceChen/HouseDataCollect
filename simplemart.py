import requests
from bs4 import BeautifulSoup
from src import function as func
from src import bo
import json

def Extract(path):
    print("====simplemart====")
    alldata = []
    url = "https://www.simplemart.com.tw/ec99/ushop20097/plusData.asp?ty=4&ptype=%E7%BE%8E%E5%BB%89%E7%A4%BE&pcity=&parea=&pname=&pKey=&rnd=0.7923799284603024"
    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text,features="lxml")


    for i in soup.find_all("ul"):
        try:
            name = i.find("li",{"class":"map-name"}).text
            time = i.find("li",{"class":"map-time"}).text
            tel = i.find("li",{"class":"map-tel"}).text
            add = i.find("li",{"class":"map-add"}).text
            alldata.append([name,time,tel,add])
        except Exception as e:
            continue


    output = path+'/simplemart.csv'
    func.writetofile(output,alldata)

def Transform(file):
    raw = func.readcsv(file)
    data = []
    idx = 1
    for r in raw:
        xy = func.transgeo(r[3],"./geo")
        row = [idx]+r + [xy['city'],xy['town'],xy['address'],xy['area'],xy['code2'],xy['code1'],xy['codebase'],xy['code'],xy['desc'],xy['x'],xy['y'],func.towkt(xy['x'],xy['y'])]
      
        data.append(row)
        idx = idx +1
    return data

if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    # Transform
    data = Transform('./data/simplemart.csv')

    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "simplemart"
    bo.load(db,table,schema[table],data)    

