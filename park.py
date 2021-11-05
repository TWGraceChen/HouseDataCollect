import requests


for i in range(14636,14660):

    url = "https://www.hpa.gov.tw/Pages/ashx/File.ashx?FilePath=~/File/Attach/12727/File_"+str(i)+".csv"
    req = requests.get(url) 
    url_content = req.content
    try:
        c = url_content
        url_content_d = c.decode("utf-8")
    except Exception as e:
        try:
            url_content_d = url_content.decode("big5").encode("utf-8")
            csv_file = open('./data/park/'+str(i)+'.csv', 'wb')
            csv_file.write(url_content_d)
            csv_file.close()
        except Exception as e:
            print(e)

print("====Finish====")
