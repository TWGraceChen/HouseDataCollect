import requests
from bs4 import BeautifulSoup
import csv


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

# write to file
with open('./data/rtmart.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(alldata)


print("====Finish====")