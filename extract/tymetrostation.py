import requests
import function as func

def Extract(path):
    print("====tymetrostation====")
    url = "https://www.rb.gov.tw/public/files/artsinfo/1607418282-m0.csv"
    req = requests.get(url) 
    url_content = req.content.decode('utf-8')

    output = path+'/tymetrostation.csv'
    func.writetofile(output,url_content)


if __name__ == '__main__':
    Extract('../data')