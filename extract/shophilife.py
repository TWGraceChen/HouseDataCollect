import requests
from bs4 import BeautifulSoup
import function as func




def refresh(url):
    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text,features="lxml")
    formdata = {'__VIEWSTATE':soup.find("input",{'id':'__VIEWSTATE'}).get("value"),
                '__EVENTVALIDATION':soup.find("input",{'id':'__EVENTVALIDATION'}).get("value"),
                '__VIEWSTATEGENERATOR':soup.find("input",{'id':'__VIEWSTATEGENERATOR'}).get("value"),
                '__EVENTTARGET':'CITY'}
    return formdata


def Extract(path):
    print("====shophilife====")
    url = "https://www.hilife.com.tw/storeInquiry_street.aspx"
    form = refresh(url)
    response = requests.request("POST", url, data=form)
    soup = BeautifulSoup(response.text,features="lxml")
    citydict = {}
    for i in soup.find("select",{"id":"CITY"}).find_all("option"):
        city = i.text
        cityform = form
        cityform['CITY']=city
        response = requests.request("POST", url,data=cityform)
        soup2 = BeautifulSoup(response.text,features="lxml")
        arealist = []
        for j in soup2.find("select",{"id":"AREA"}).find_all("option"):
            area = j.text
            arealist.append(area)

        citydict[city] = arealist    

    alldata = []
    for city in citydict:
        cityform = form
        cityform['CITY']=city
        for area in citydict[city]:
            print(city+area)
            areaform = cityform
            areaform['AREA'] = area
            try:
                try:
                    response = requests.request("POST", url, data=areaform)
                except:
                    form = refresh(url)
                    cityform = form
                    cityform['CITY']=city
                    areaform = cityform
                    areaform['AREA'] = area
                    response = requests.request("POST", url, data=areaform)

                soup3 = BeautifulSoup(response.text,features="lxml")
                for k in soup3.find_all('tr'):
                    id = k.find_all('th')[0].text
                    name = k.find_all('th')[1].text
                    address = k.find('a').text
                    services = []
                    for l in k.find_all('img'):
                        if l.get("title") != None:
                            services.append(l.get("title"))
                    data = [city,area,id,name,address,",".join(services)]
                    alldata.append(data)
            except Exception as e:
                print(e)

    output = path+'/shophilife.csv'
    func.writetofile(output,alldata)


if __name__ == '__main__':
    Extract('../data')
