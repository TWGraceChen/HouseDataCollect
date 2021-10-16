import requests

url = "	https://data.nhi.gov.tw/DataSets/DataSetResource.ashx?rId=A21030000I-D21005-001"
req = requests.get(url)
url_content = req.content
csv_file = open('./data/pharmarcy.csv', 'wb')
csv_file.write(url_content)
csv_file.close()
print("====Finish====")
