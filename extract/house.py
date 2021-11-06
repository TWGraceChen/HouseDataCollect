import requests, zipfile, io



def Extract(path):
    print("====house====")
    y = 101
    stop = False
    while stop != True:
        for s in [1,2,3,4]:
            period = "%sS%s"%(y,s)
            print("downloading:"+period)
            url = "https://plvr.land.moi.gov.tw//DownloadSeason?season=" + period + "&type=zip&fileName=lvr_landcsv.zip"
            try:
                output = path+"/house/"+period
                r = requests.get(url)
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall(output)
                print("save csv:" + output)
            except:
                stop = True
                break
        y = y + 1

if __name__ == '__main__':
    Extract('../data')