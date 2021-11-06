import requests
from bs4 import BeautifulSoup
import csv
import json
import xml.etree.ElementTree as ET



def writetofile(output,data):
    if isinstance(data,str):
        csv_file = open(output, 'w')
        csv_file.write(data)
        csv_file.close()
    else:
        with open(output, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
    print("save csv:" + output)



