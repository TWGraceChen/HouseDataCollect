import requests, zipfile, io
from os import replace



def Extract(path):
    print("====hospital====")
    url = "https://www.nhi.gov.tw/DL.aspx?sitessn=292&u=LzAwMS9VcGxvYWQvMjkyL3JlbGZpbGUvMC84NDY3L2hvc3Bic2Muemlw&n=aG9zcGJzYy56aXA%3d"
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(path)
    output = path+"/hospital.csv"
    replace(path+"/hospbsc.txt",output )
    print("save csv:" + output)

if __name__ == '__main__':
    Extract('../data')