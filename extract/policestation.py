import requests
import zipfile
import io,os
import shutil



def Extract(path):
    print("====policestation====")
    url = "	https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=EE144E5A-39DE-4A20-9654-B295EB9F9F19"

    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))

    dirname = path+"/policestation/"
    z.extractall(dirname)
    
    output = path+"/policestation.csv"
    for filename in os.listdir(dirname):
        if "Address" in filename:
            shutil.move(dirname+filename, output)
            print("save csv:" + output)
    shutil.rmtree(dirname)


if __name__ == '__main__':
    Extract('../data')

    