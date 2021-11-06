import requests
import xml.etree.ElementTree as ET
import function as func



def Extract(path):
    print("====shopseven====")
    alldata = []
    url = "https://emap.pcsc.com.tw/EMapSDK.aspx"

    citylist = {'01':'台北市','02':'基隆市','03':'新北市','04':'桃園市','05':'新竹市','06':'新竹縣','07':'苗栗縣','08':'台中市','10':'彰化縣','11':'南投縣','12':'雲林縣','13':'嘉義市','14':'嘉義縣','15':'台南市','17':'高雄市','19':'屏東縣','20':'宜蘭縣','21':'花蓮縣','22':'台東縣','23':'澎湖縣','24':'連江縣','25':'金門縣'}
    for cityid in citylist:
        city = citylist[cityid]
        # get town in city
        payload={'commandid': 'GetTown','cityid': cityid}
        response = requests.request("POST", url,data=payload)
        townxml = ET.fromstring(response.text)
        for x in townxml.findall('GeoPosition'):
            towmid = x.find("TownID").text
            townname = x.find("TownName").text
            townx = x.find("X").text
            towny = x.find("Y").text

            # get shop in town
            payload={'commandid': 'SearchStore','city': city,'town': townname}
            response = requests.request("POST", url, data=payload)
            shopxml = ET.fromstring(response.text)
            for y in shopxml.findall('GeoPosition'):
                poiid = y.find("POIID").text.strip()
                poiname = y.find("POIName").text
                poix = y.find("X").text
                poiy = y.find("Y").text
                poitelno = y.find("Telno").text.strip()
                poifaxno = y.find("FaxNo").text.strip()
                poiaddress = y.find("Address").text
                poiimg = y.find("StoreImageTitle").text
                data = [cityid,city,towmid,townname,townx,towny,poiid,poiname,poix,poiy,poitelno,poifaxno,poiaddress,poiimg]
                alldata.append(data)
            print(city+townname)

    output = path+'/shop7-11.csv'
    func.writetofile(output,alldata)


if __name__ == '__main__':
    Extract('../data')

    
   