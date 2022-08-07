# -*- coding: utf-8 -*-
"""
@author: Hank
"""
import requests
import json
from src import function as func
import sys
from src import bo
import re

def Extract(path):
    print("====funeralfacilities====")
    url = "https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=0CA9D125-A3F2-446C-B27D-EF691A9701E5"
    req = requests.get(url)
    url_content = req.content.decode('utf-8').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)
    content_data = json.loads(url_content)
    
    alldata = []
    column = ["facilityId", "facilityName", "facilityClass", "facilityType", "belongCityId", "phone", "fax", "url", "email", "address"] 
    #no photo and facility_service
    alldata.append(column) #csv欄位
    
    for data in content_data:
        list = []
        for i in range(len(column)):
            if column[i] in data:
                list.append(str(data[column[i]]))
        alldata.append(list)

    output = path+'/funeralfacilities.csv'
    func.writetofile(output,alldata)


def Transform(file):
    # facilityId,facilityName,facilityClass,facilityType,belongCityId,phone,fax,url,email,address
    raw = func.readcsv(file)
    raw = raw[1:]
    data = [] 
    idx = 1
    for r in raw:
        row = r
        if len(r) < 10:
            continue
        if len(r[9]) > 0:
            address = re.sub("\(.+\)", "", r[9])
            xy = func.transgeo(address,"./geo")
            row = row + [xy['city'],xy['town'],xy['address'],xy['area'],xy['code2'],xy['code1'],xy['codebase'],xy['code'],xy['desc'],xy['x'],xy['y'],func.towkt(xy['x'],xy['y'])]
        else:
            row = row + [""] * 12
        data.append([idx]+row)
        idx = idx +1
        
    return data

if __name__ == '__main__':
    # Extract
    #Extract('./data')

    # Transform
    data = Transform('./data/funeralfacilities.csv')
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "funeralfacilities"
    bo.load(db,table,schema[table],data)