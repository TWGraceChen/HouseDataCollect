import requests
from requests.packages import urllib3
import function as func

def Extract(path):
    print("====eco====")
    urllib3.disable_warnings()
    url = "https://apiservice.mol.gov.tw/OdService/download/A17030000J-000016-wWs"
    response = requests.request("GET", url, verify=False)
    content = response.content.decode('utf-8')
    output = path+'/eco.csv'  
    func.writetofile(output,content)  




if __name__ == '__main__':
    Extract('../data')