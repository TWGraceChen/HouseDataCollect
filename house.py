import requests, zipfile, io
from src import function as func
from src import bo
import json
import csv

def ymtodt(ym):
    if len(ym) < 7:
        return "2000-00-00"
    y = int(ym[:3]) + 1911
    return "{}-{}-{}".format(y,ym[3:5],ym[5:7])

def filladdress(city,town,address):
    if city in address and town in address:
        return address
    else:
        return city+town+address

def Extract(path):
    print("====house====")
    y = 101
    stop = False
    while stop != True:
        for s in [1,2,3,4]:
            period = "%sS%s"%(y,s)
            print("downloading:"+period)
            url = "https://plvr.land.moi.gov.tw//DownloadSeason?season=" + period + "&type=zip&fileName=lvr_landcsv.zip"
            try:
                output = path+"/house/"+period
                r = requests.get(url)
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall(output)
                print("save csv:" + output)
            except:
                stop = True
                break
        y = y + 1


def Transform(path,cate):
    city = {"c":"基隆市","a":"臺北市","f":"新北市","h":"桃園市","o":"新竹市","j":"新竹縣","k":"苗栗縣","b":"臺中市","m":"南投縣","n":"彰化縣","p":"雲林縣","i":"嘉義市","q":"嘉義縣","d":"臺南市","e":"高雄市","t":"屏東縣","g":"宜蘭縣","u":"花蓮縣","v":"臺東縣","x":"澎湖縣","w":"金門縣","z":"連江縣"}
    data_a = []
    data_b = []
    data_c = []
    for c in cate:
        print("===="+c+"====")
        data = []
        for k in city:
            print("a:"+city[k])
            file = "{}/{}_lvr_land_{}.csv".format(path,k,c)
            raw = func.readcsv(file)
            raw = raw[2:]
            for r in raw:
                address = filladdress(city[k],r[0],r[2])
                if r[1] == '土地':
                    new = [city[k]] + r[0:2] + [address] + r[3:7] + [ymtodt(r[7])] + r[8:14]+[ymtodt(r[14])] + r[15:]+ [""] * 12
                else:
                    xy = func.transgeo(address,"./geo")
                    new = [city[k]] + r[0:2] + [address] + r[3:7] + [ymtodt(r[7])] + r[8:14]+[ymtodt(r[14])] + r[15:] + [xy['city'],xy['town'],xy['address'],xy['area'],xy['code2'],xy['code1'],xy['codebase'],xy['code'],xy['desc'],xy['x'],xy['y'],func.towkt(xy['x'],xy['y'])]
                data.append(new)
        #exec("data_"+c+"= data")
        if c == 'a':
            data_a = data
        elif c == 'b':
            data_b = data
        elif c == 'c':
            data_c = data
    return data_a,data_b,data_c

def Preparecsv(path,cate,period):
    city = {"c":"基隆市","a":"臺北市","f":"新北市","h":"桃園市","o":"新竹市","j":"新竹縣","k":"苗栗縣","b":"臺中市","m":"南投縣","n":"彰化縣","p":"雲林縣","i":"嘉義市","q":"嘉義縣","d":"臺南市","e":"高雄市","t":"屏東縣","g":"宜蘭縣","u":"花蓮縣","v":"臺東縣","x":"澎湖縣","w":"金門縣","z":"連江縣"}
    for c in cate:
        print("===="+c+"====")

        for k in city:
            print(c+":"+city[k])
            data = []
            file = "{}/{}_lvr_land_{}.csv".format(path,k,c)
            raw = func.readcsv(file)
            raw = raw[2:]
            id = 0
            for r in raw:
                cityname = city[k]
                townname = r[0]
                address = r[2]
                if cityname in address and townname in address:
                    address = address.replace(cityname,'').replace(townname,'')
                    
                id = id+1
                if r[1] == '土地':
                    continue
                else:
                    data.append([id,cityname,townname,'','',address])
            
            f = 1
            size = 10000
            while len(data) > 0:
                wdata = [['ID(非必填)','縣市(必填)','鄉鎮(必填)','村里(可不填)','鄰(可不填)','地址(必填)']] + data[:size]
                #func.writetofile('./geobatch/house_'+period+'_'+c+'_'+k+'_'+str(f)+'.csv',wdata)
                with open('./geobatch/house_'+period+'_'+c+'_'+k+'_'+str(f)+'.csv', 'w', newline='', encoding='Big5',errors='ignore') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(wdata)
                data = data[size:]
                f = f+1

def Preparecsvtgos(path,cate,period):
    city = {"c":"基隆市","a":"臺北市","f":"新北市","h":"桃園市","o":"新竹市","j":"新竹縣","k":"苗栗縣","b":"臺中市","m":"南投縣","n":"彰化縣","p":"雲林縣","i":"嘉義市","q":"嘉義縣","d":"臺南市","e":"高雄市","t":"屏東縣","g":"宜蘭縣","u":"花蓮縣","v":"臺東縣","x":"澎湖縣","w":"金門縣","z":"連江縣"}
    city = {"a":"臺北市","f":"新北市"}
    for c in cate:
        print("===="+c+"====")

        for k in city:
            print(c+":"+city[k])
            data = []
            file = "{}/{}_lvr_land_{}.csv".format(path,k,c)
            raw = func.readcsv(file)
            raw = raw[2:]
            id = 0
            for r in raw:
                address = filladdress(city[k],r[0],r[2])
                id = id+1
                if r[1] == '土地':
                    continue
                else:
                    data.append([id,address,'','',''])
            
            f = 1
            size = 10000
            while len(data) > 0:
                wdata = [["id","Address","Response_Address","Response_X","Response_Y"]] + data[:size]
                #func.writetofile('./geobatchtgos/house_'+period+'_'+c+'_'+k+'_'+str(f)+'.csv',wdata)
                with open('./geobatchtgos/house_'+period+'_'+c+'_'+k+'_'+str(f)+'.csv', 'w', newline='', encoding='Big5',errors='ignore') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(wdata)
                data = data[size:]
                f = f+1               

if __name__ == '__main__':
    # Extract
    #Extract('./data')
    

    # Prepare Upload Data
    period = "108S4"
    path = './data/house/'+period
    category = ['a']
    #Preparecsv(path,category,period)
    Preparecsvtgos(path,category,period)
    
    ## Transform
    #data_a,data_b,data_c = Transform(path,category)


    ## Load
    #db = bo.conn("127.0.0.1",13303,period)
    #with open("schema.json") as f:
    #    schema = json.load(f)
    #table = "house_buy"
    #bo.load(db,table,schema[table],data_a) 
    #table = "house_pre_buy"
    #bo.load(db,table,schema[table],data_b)  
    #table = "house_rent"
    #bo.load(db,table,schema[table],data_c)    