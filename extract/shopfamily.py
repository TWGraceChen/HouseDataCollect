import requests
import json
import function as func


def Extract(path):
    print("====shopfamily====")
    alldata = []
    citylist = ['台北市','基隆市','新北市','桃園市','新竹市','新竹縣','苗栗縣','台中市','彰化縣','南投縣','雲林縣','嘉義市','嘉義縣','台南市','高雄市','屏東縣','宜蘭縣','花蓮縣','台東縣','澎湖縣','連江縣','金門縣']
    for city in citylist:
        # get town in city
        url = "https://api.map.com.tw/net/familyShop.aspx?searchType=ShowTownList&type=&city="+city+"&fun=storeTownList&key=6F30E8BF706D653965BDE302661D1241F8BE9EBC"
        headers = {'Referer': 'https://www.family.com.tw/'}
        response = requests.request("GET", url, headers=headers)
        obj = json.loads(response.text[14:-1])
        for townobj in obj:
            # get shop in town
            post = townobj["post"]
            town = townobj["town"]
            url = "https://api.map.com.tw/net/familyShop.aspx?searchType=ShopList&type=&city="+city+"&area="+town+"&road=&fun=showStoreList&key=6F30E8BF706D653965BDE302661D1241F8BE9EBC"
            headers = {'Referer': 'https://www.family.com.tw/'}
            response = requests.request("GET", url, headers=headers)
            shopobj = json.loads(response.text[14:-1])
            for shop in shopobj:
                name = shop["NAME"]
                tel = shop["TEL"]
                postel = shop["POSTel"]
                px = shop["px"]
                py = shop["py"]
                addr = shop["addr"]
                serid = shop["SERID"]
                pkey = shop["pkey"]
                oldpkey = shop["oldpkey"]
                post2 = shop["post"]
                services = shop["all"]
                road = shop["road"]
                twoice = shop["twoice"]
                data = [post,town,name,tel,postel,px,py,addr,serid,pkey,oldpkey,post2,services,road,twoice]
                alldata.append(data)
            print(city+town)

    output = path+'/shopfamily.csv'
    func.writetofile(output,alldata)

if __name__ == '__main__':
    Extract('../data')

    
   

