import requests
from html.parser import HTMLParser
import csv

class HTMLCleaner(HTMLParser):
    def __init__(self, *args, **kwargs):
        super(HTMLCleaner, self).__init__(*args, **kwargs)
        self.data_list = []

    def handle_data(self, data):
        self.data_list.append(data)

alldata = []
citylist = ['台北市','基隆市','新北市','桃園市','新竹市','新竹縣','苗栗縣','台中市','彰化縣','南投縣','雲林縣','嘉義市','嘉義縣','台南市','高雄市','屏東縣','宜蘭縣','花蓮縣','台東縣','澎湖縣','連江縣','金門縣']
for city in citylist:
    print(city)
    url = "https://www.okmart.com.tw/convenient_shopSearch_Result.aspx?city="+city
    response = requests.request("GET", url)
    parser = HTMLCleaner()
    parser.feed(response.text)
    
    counter = 1
    data = []
    for cell in parser.data_list[1:]:
        data.append(cell.strip())
        if counter == 4:
            alldata.append(data)
            data = []
            counter = 0
        counter = counter + 1


# write to file
with open('./data/shopokmart.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(alldata)
