import requests, zipfile, io
from os import replace


url = "https://www.nhi.gov.tw/DL.aspx?sitessn=292&u=LzAwMS9VcGxvYWQvMjkyL3JlbGZpbGUvMC84NDY3L2hvc3Bic2Muemlw&n=aG9zcGJzYy56aXA%3d"
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall("./data")
replace("./data/hospbsc.txt", "./data/hospital.csv")

print("====Finish====")