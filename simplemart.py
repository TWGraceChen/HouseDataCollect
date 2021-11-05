import requests
from bs4 import BeautifulSoup
import csv


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

# write to file
with open('./data/simplemart.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(alldata)


print("====Finish====")