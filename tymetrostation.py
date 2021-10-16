import requests

url = "https://www.rb.gov.tw/public/files/artsinfo/1607418282-m0.csv"
req = requests.get(url) 
url_content = req.content
csv_file = open('./data/tymetrostation.csv', 'wb')
csv_file.write(url_content)
csv_file.close()
print("====Finish====")
