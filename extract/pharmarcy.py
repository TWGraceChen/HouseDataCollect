import requests
import function as func

def Extract(path):
    print("====pharmarcy====")
    url = "	https://data.nhi.gov.tw/DataSets/DataSetResource.ashx?rId=A21030000I-D21005-001"
    req = requests.get(url)
    url_content = req.content.decode('utf-8')
    output = path+'/pharmarcy.csv'
    func.writetofile(output,url_content)




if __name__ == '__main__':
    Extract('../data')