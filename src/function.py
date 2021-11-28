import requests
from bs4 import BeautifulSoup
import csv
import json
import xml.etree.ElementTree as ET
import requests
import urllib.parse
import twd97


def writetofile(output,data):
    if isinstance(data,str):
        csv_file = open(output, 'w')
        csv_file.write(data)
        csv_file.close()
    else:
        with open(output, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
    print("save csv:" + output)


def readcsv(file,encode='utf8'):
    with open(file, newline='', encoding=encode) as csvfile:
        rows = csv.reader(csvfile)
        return list(rows)

def transgeo(address,path):
    filename = path+'/'+address.replace("/","_")+'.json'
    try:
        with open(filename) as f:
            r = json.load(f)
            return r
    except Exception as e:
        None
    print("search:"+address)
    encodeaddr = urllib.parse.quote(address)

    url = "https://moisagis.moi.gov.tw/moiap/gis2010/content/user/matchservice/singleMatch.cfm"
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    payload = "address=" + encodeaddr + "&matchRange=0&fuzzyNum=0&roadEQstreet=false&subnumEQnum=false&isLockTown=false&isLockVillage=false&ex_coor=EPSG%3A4326&U02DataYear=2015&output_xml=1"
    response = requests.request("POST", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text,features="lxml")
    try:
        result = soup.find("tr",{"class":"bwhite"}).find_all("td")
        r = {
            'city':result[0].text,
            'town':result[1].text,
            'address':result[2].text,
            'area':result[3].text,
            'code2':result[4].text,
            'code1':result[5].text,
            'codebase':result[6].text,
            'code':result[7].text,
            'desc':result[8].text,
            'x':result[9].text,
            'y':result[10].text
        }
        with open(filename, 'w') as f:
            json.dump(r, f)
    except Exception as e:
        print(e)
        r = {
            'city':"",
            'town':"",
            'address':"",
            'area':"",
            'code2':"",
            'code1':"",
            'codebase':"",
            'code':"",
            'desc':"",
            'x':"",
            'y':""
        }
    
    return r



def transgeoxy(x,y):
    url = "https://moisagis.moi.gov.tw/moiap/gis2010/content/user/matchservice/singleMatch_xy.cfm"

    payload = "match_x="+str(x)+"&match_y="+str(y)+"&coor_sys=EPSG%3A4326&codeDataYear=2015"
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    response = requests.request("POST", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text,features="lxml")
    result = soup.find("tr",{"class":"bwhite"}).find_all("td")
    
    r = {
        'city':result[0].text,
        'town':result[1].text,
        'area':result[2].text,
        'code2':result[3].text,
        'code1':result[4].text,
        'codebase':result[5].text,
        'x':result[6].text,
        'y':result[7].text}
    return r


def TWDToGPS(lon,lat):
    r = twd97.towgs84(lon, lat)
    return list(r)


if __name__ == '__main__':
    #print(transgeo("臺北市大同區甘州街51號","../geo"))
    #print(transgeoxy(121.514055,25.048808))
    print(TWDToGPS(301442.6468,2770733.688))
