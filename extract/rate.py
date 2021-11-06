import requests
import function as func


def Extract(path):
    print("====rate====")
    url = "	https://www.cbc.gov.tw/public/data/OpenData/A13Rate.csv"
    content = requests.get(url).content.decode('utf-8')
    output = path+'/rate.csv'
    func.writetofile(output,content)



if __name__ == '__main__':
    Extract('../data')

    
