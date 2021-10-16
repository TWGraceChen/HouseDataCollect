import requests, zipfile, io

y = 101
stop = False
while stop != True:
    for s in [1,2,3,4]:
        period = "%sS%s"%(y,s)
        print("downloading:"+period)
        url = "https://plvr.land.moi.gov.tw//DownloadSeason?season=" + period + "&type=zip&fileName=lvr_landcsv.zip"
        try:
            r = requests.get(url)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall("./data/house/"+period)
        except:
            stop = True
            break
    y = y + 1
print("====Finish====")