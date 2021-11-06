import bo
import csv
import os


def load(db,file,table,skip=0):
    try:
        with open(file, encoding="utf8") as csvfile:
            data = list(csv.reader(csvfile))
    except:
        with open(file, encoding="utf-16") as csvfile:
            data = list(csv.reader(csvfile))

    data = data[skip:]
    l = len(data[0])
    sql = "create table `"+ table + "`("
    for c in range(1,l +1):
        sql = sql + "col_" + str(c) + " varstring,"

    sql = sql[:-1] + ")"
    try:
        bo.exec(db,sql)
    except Exception as e:
        None

    values = []
    for rows in data:
        values.append("(" + ",".join(["\""+str(item).replace("\"","\\\"")+"\"" for item in rows]) + ")")
        if len(values) == 300 or len(values) == len(data):
            sql = "insert into `" + table + "` values "+ ",".join(values)
            try:
                bo.exec(db,sql)
            except Exception as e:
                print(sql)
            values = []
        
    print(file,"--->",table)


path = "../data"
db = bo.conn("127.0.0.1",13303,"house")


for filename in os.listdir(path):
    if os.path.isdir(path+"/"+filename):
        continue
    print(filename)
    try:
        load(db,path+"/"+filename,filename.split(".")[0])
    except Exception as e:
        print(e)

pathpark = path+"/park"
for filename in os.listdir(pathpark):
    print(filename)
    try:
        load(db,pathpark+"/"+filename,"park",1)
    except Exception as e:
        print(e)


pathschool = path+"/school"
for filename in os.listdir(pathschool):
    print(filename)
    try:
        load(db,pathschool+"/"+filename,filename.split(".")[0],1)
    except Exception as e:
        print(e)

pathhouse = path+"/house"
for subpath in os.listdir(pathhouse):
    db = bo.conn("127.0.0.1",13303,subpath)
    for filename in os.listdir(pathhouse+"/"+subpath):
        if filename == "build.ttt" or "schema" in filename or filename == "manifest.csv":
            continue
        try:
            load(db,pathhouse+"/"+subpath+"/"+filename,filename[2:].split(".")[0],2)
        except Exception as e:
            print(e)