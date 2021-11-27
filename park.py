import requests
from bs4 import BeautifulSoup
import json
from src import function as func
import os

def Extract(path):
    print("====park====")
    cate_url = "https://data.gov.tw/dataset/31163"
    response = requests.request("GET", cate_url)
    soup = BeautifulSoup(response.text,features="lxml")
    f = soup.find("script",{"data-n-head":"ssr","type":"application/ld+json"})
    content = json.loads(f.text)
    

    try:
        os.mkdir(path+"/park")
    except Exception as e:
        None

    for i in content[1]["distribution"]:
        url = i["contentUrl"]
        res = requests.request("GET", url)
        url_content = res.content
        try:
            url_content_d = url_content.decode("big5")
            output = path+"/park/"+url.split("/")[-1]
            func.writetofile(output,url_content_d)
        except Exception as e:
            print(e)



if __name__ == '__main__':
    Extract('../data')