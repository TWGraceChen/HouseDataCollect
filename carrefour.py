
import requests
import json
from src import function as func
from src import bo

def Extract(path):
  print("====carrefour====")
  alldata = []
  url = "https://www.carrefour.com.tw/console/api/v1/stores?page_size=all"
  response = requests.request("GET", url)

  for row in json.loads(response.content)['data']['rows']:
    data = [row['id'],row['name'],row['is24h'],row['iscibc'],row['status'],row['status_name'],row['code'],row['sn'],row['sort'],row['store_area_id'],row['store_group_id'],row['store_type_id'],row['store_area_name'],row['store_group_name'],row['store_type_name'],row['fb'],row['line'],row['contact_name'],row['contact_email'],row['contact_tel'],row['contact_tel_ext'],row['contact_fax'],row['area_id'],row['city_id'],row['street'],row['area_name'],row['city_name'],row['address'],row['cibc_address'],row['latitude'],row['longitude'],row['business_hours'],row['business_hours_special'],row['parking_info'],row['parking_spaces_moto'],row['parking_spaces_car'],row['parking_spaces_handicapped'],row['parking_spaces_parent'],row['bus_info'],row['traffic_info'],row['en_name'],row['en_business_hours'],row['en_business_hours_special'],row['en_street'],row['en_parking_info'],row['en_bus_info'],row['en_traffic_info'],row['scs_number'],row['scs_number_id'],row['mon_start'],row['mon_end'],row['tue_start'],row['tue_end'],row['wed_start'],row['wed_end'],row['thur_start'],row['thur_end'],row['fri_start'],row['fri_end'],row['sat_start'],row['sat_end'],row['sun_start'],row['sun_end'],row['store_link'],row['scango_flg'],row['created_at'],row['updated_at']]
    alldata.append(data)

  output = path+'/carrefour.csv'
  func.writetofile(output,alldata)

def Transform(file):
    raw = func.readcsv(file)
    data = []
    for r in raw:
      data.append(r+[func.towkt(r[30],r[29])])
    return data


if __name__ == '__main__':
    # Extract
    Extract('./data')
    
    ## Transform
    data = Transform('./data/carrefour.csv')

    ## Load
    db = bo.conn("127.0.0.1",13303,"house")
    with open("schema.json") as f:
        schema = json.load(f)
    table = "carrefour"
    bo.load(db,table,schema[table],data)    