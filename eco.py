import requests
from requests.packages import urllib3

urllib3.disable_warnings()

url = "https://apiservice.mol.gov.tw/OdService/download/A17030000J-000016-wWs"
response = requests.request("GET", url, verify=False)
content = response.content


csv_file = open('./data/eco.csv', 'wb')
csv_file.write(content)
csv_file.close()

print("====Finish====")
