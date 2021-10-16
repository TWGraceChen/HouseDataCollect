import requests
from openpyxl import load_workbook
import csv
import os


def process(url,name):
    req = requests.get(url)
    url_content = req.content
    f = open('./data/'+name+'.xlsx', 'wb')
    f.write(url_content)
    f.close()

    wb = load_workbook('./data/'+name+'.xlsx')
    dataset = []
    for sheet in wb:
        for row in sheet.iter_rows():
            data = []
            for cell in row:
                data.append(cell.value)
            dataset.append(data)

    # write to file
    with open('./data/'+name+'.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(dataset)

    os.remove('./data/'+name+'.xlsx') 

process("https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=F412EAC2-1953-40BA-8AF3-A7A45EE253E3",'firestation1') 
process("https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=C38B7AC2-E7F3-4DD5-A3F3-88E623B55924",'firestation2') 

print("====Finish====")
