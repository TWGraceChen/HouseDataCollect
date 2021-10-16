import requests, zipfile, io

for y in range(101,110):
    for s in range(1,5):
        period = "%sS%s"%(y,s)
        print("downing:"+period)
        url = "https://plvr.land.moi.gov.tw//DownloadSeason?season=" + period + "&type=zip&fileName=lvr_landcsv.zip"
        r = requests.get(url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("./data/house/"+period)

print("====Finish====")