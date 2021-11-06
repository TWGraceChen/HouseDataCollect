import requests
from bs4 import BeautifulSoup
import csv
import json
import xml.etree.ElementTree as ET

# 最小統計區
alldata_base = []
# 一級發布區
alldata_1 = []
# 二級發布區
alldata_2 = []

cate_url = "https://data.gov.tw/dataset/18681"
response = requests.request("GET", cate_url)
soup = BeautifulSoup(response.text,features="lxml")
f = soup.find("script",{"data-n-head":"ssr","type":"application/ld+json"})
content = json.loads(f.text)

for i in content[1]["distribution"]:
    url = i["contentUrl"]
    print(url)
    res = requests.request("GET", url)
    xml = ET.fromstring(res.content)
    for data in xml.find("RowDataList").findall("RowData"):
        INFO_TIME = data.find("INFO_TIME").text
        H_CNT = data.find("H_CNT").text
        P_CNT = data.find("P_CNT").text
        M_CNT = data.find("M_CNT").text
        F_CNT = data.find("F_CNT").text
        CODE2 = data.find("CODE2").text
        
        if data.find("CODEBASE") != None:
            CODEBASE = data.find("CODEBASE").text
            CODE1 = data.find("CODE1").text
            alldata_base.append([INFO_TIME,CODE2,CODE1,CODEBASE,H_CNT,P_CNT,M_CNT,F_CNT])
        elif data.find("CODE1") != None:
            CODE1 = data.find("CODE1").text
            alldata_1.append([INFO_TIME,CODE2,CODE1,H_CNT,P_CNT,M_CNT,F_CNT])
        else:
            alldata_2.append([INFO_TIME,CODE2,H_CNT,P_CNT,M_CNT,F_CNT])

# write to file
with open('./data/people_base.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(alldata_base)

with open('./data/people_1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(alldata_1)

with open('./data/people_2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(alldata_2)

print("====Finish====")