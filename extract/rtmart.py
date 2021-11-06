import requests
from bs4 import BeautifulSoup
import function as func


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


if __name__ == '__main__':
    Extract('../data')

    
