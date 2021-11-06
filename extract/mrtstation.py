import requests
import function as func

def Extract(path):
    print("====mrtstation====")
    url = "https://data.taipei/api/getDatasetInfo/downloadResource?id=cfa4778c-62c1-497b-b704-756231de348b&rid=42694bb8-fc9d-4d82-af7a-0ad6f4c9ad57"
    req = requests.get(url)
    url_content = req.content.decode('big5')
    
    output = path+"/mrtstation.csv"
    func.writetofile(output,url_content)


if __name__ == '__main__':
    Extract('../data')


