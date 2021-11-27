from requests import request
import json
from hashlib import sha1
import hmac
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import base64
from src import function as func
from src import bo

alldata = []
citylist = {'Taipei':'臺北市','Keelung':'基隆市','NewTaipei':'新北市','Taoyuan':'桃園市',
            'Hsinchu':'新竹市','HsinchuCounty':'新竹縣','MiaoliCounty':'苗栗縣',
            'Taichung':'臺中市','ChanghuaCounty':'彰化縣','NantouCounty':'南投縣',
            'YunlinCounty':'雲林縣','Chiayi':'嘉義市','ChiayiCounty':'嘉義縣','Tainan':'臺南市',
            'Kaohsiung':'高雄市','PingtungCounty':'屏東縣',
            'YilanCounty':'宜蘭縣','HualienCounty':'花蓮縣','TaitungCounty':'台東縣',
            'PenghuCounty':'澎湖縣','LienchiangCounty':'連江縣','KinmenCounty':'金門縣'}


class Auth():
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_auth_header(self):
        xdate = format_date_time(mktime(datetime.now().timetuple()))
        hashed = hmac.new(self.app_key.encode('utf8'), ('x-date: ' + xdate).encode('utf8'), sha1)
        signature = base64.b64encode(hashed.digest()).decode()

        authorization = 'hmac username="' + self.app_id + '", ' + \
                        'algorithm="hmac-sha1", ' + \
                        'headers="x-date", ' + \
                        'signature="' + signature + '"'
        return {
            'Authorization': authorization,
            'x-date': format_date_time(mktime(datetime.now().timetuple())),
            'Accept - Encoding': 'gzip'
        }

def updatetime(t):
    d = datetime.strptime(t, '%Y-%m-%dT%H:%M:%S+08:00')
    return datetime.strftime(d, '%Y-%d-%m %H:%M:%S')


def getvalue(data,key):
    try:
        value = data[key]
    except:
        value = ''
    return value


def Extract(path,key):
    print("====busstation====")
    with open(key, newline='') as jsonfile:
        data = json.load(jsonfile)
        app_id = data['appid']
        app_key = data['appkey']
    
    a = Auth(app_id, app_key)
    for cityid in citylist:
        url = 'https://ptx.transportdata.tw/MOTC/v2/Bus/Stop/City/'+cityid+'?$format=JSON&'
        city = citylist[cityid]
        print("==="+city+"===") 
        response = request('get', url, headers= a.get_auth_header())
    
        for stop in json.loads(response.content):
            StopUID = stop['StopUID']
            StopID = stop['StopID']
            AuthorityID = stop['AuthorityID']
            StopName_tw = stop['StopName']['Zh_tw']
            StopName_En = getvalue(stop['StopName'],'En')
            lon = stop['StopPosition']['PositionLon']   
            lat = stop['StopPosition']['PositionLat']
            geohash = stop['StopPosition']['GeoHash']
            StopAddress = getvalue(stop,'StopAddress')
            Bearing = getvalue(stop,'Bearing')
            StationID = getvalue(stop,'StationID')
            City = stop['City']
            CityCode = stop['CityCode']
            LocationCityCode = stop['LocationCityCode']
            UpdateTime = updatetime(stop['UpdateTime'])
            VersionID = stop['VersionID']
            data = [city,StopUID,StopID,AuthorityID,StopName_tw,StopName_En,lon,lat,geohash,StopAddress,Bearing,StationID,City,CityCode,LocationCityCode,UpdateTime,VersionID]
            alldata.append(data)
    
    
    output = path+'/busstation.csv'
    func.writetofile(output,alldata)


def Transform(file):
    return func.readcsv(file)

if __name__ == '__main__':
    # Extract
    Extract('./data',"ptxkey.json")
    
    # Transform
    data = Transform('./data/busstation.csv')
    
    # Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "busstation"
    bo.load(db,table,schema[table],data)