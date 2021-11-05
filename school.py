import requests
import os

datalist = {
    "學前教保服務機構幼兒園":"k1_new.csv",
    "互助教保服務中心":"k2_new.csv",
    "國民小學":"e1_new.csv",
    "國民中學":"j1_new.csv",
    "附設國小部":"ac.csv",
    "附設國中部":"aj_new.csv",
    "偏遠地區學校國中小":"faraway1.csv",
    "偏遠地區學校高中":"faraway2.csv",
    "偏遠地區學校其他":"faraway3.csv",
    "原住民族地區國小":"native_new.csv",
    "高級中等學校一般高級中等學校":"high.csv",
    "高級中等學校大專附設進修學校":"highT.csv",
    "高級中等學校大專附設高職部":"highA.csv",
    "高級中等學校其他":"highO.csv",
    "大專校院":"u1_new.csv",
    "宗教研修學院":"u3_new.csv",
    "空大及大專附設進修學校":"u2_new.csv",
    "特殊教育學校":"sp1_new.csv",
    "國中小補校":"s2_new.csv",
    "軍警大專校院":"school08_new.csv",
    "大陸臺商子弟學校與海外臺灣學校名錄":"school04_new.csv",
    "非學校型態實驗教育機構":"school_exp.csv"
}

path = "./data/school"
try:
    os.mkdir(path)
except Exception as e:
    None

for k in datalist:
    print(k)
    baseurl = "https://stats.moe.gov.tw/files/school/109/"
    url = baseurl + datalist[k]
    content = requests.get(url).content
    csv_file = open(path+ '/' + k + '.csv', 'wb')
    csv_file.write(content)
    csv_file.close()

print("====Finish====")
