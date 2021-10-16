import requests
import zipfile
import io,os
import shutil

url = "	https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=EE144E5A-39DE-4A20-9654-B295EB9F9F19"

r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))

dirname = "./data/policestation/"
z.extractall(dirname)

for filename in os.listdir(dirname):
    if "Address" in filename:
        shutil.move(dirname+filename, "./data/policestation.csv")
shutil.rmtree(dirname)
print("====Finish====")