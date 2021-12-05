import pymysql


def conn(host,port,db):
    db_settings = {
        "host": host,
        "port": port,
        "user": "root",
        "password": "",
        "db": db,
        "charset": "utf8",
        "connect_timeout":31536000
    }

    try:
        conn = pymysql.connect(**db_settings)
        print("success connect to bo!!")
        exec(conn,"create database "+ db)
    except Exception as ex:
        conn = None
        print(ex)
    return conn


def exec(conn,command):
    with conn.cursor() as cursor:
        cursor.execute(command)


def insertdb(conn,table,schema,data):
    sql = "create table "+ table + "("+schema+")"
    try:
        exec(conn,sql)
    except Exception as e:
        print(e)

    values = data.values.tolist()
    dataset = []
    for value in values:
        dataset.append("("+",".join(['"'+str(item).replace("\"","\\\"")+'"' for item in value])+")")
    sql = "insert into "+ table + " values "+",".join(dataset)
    exec(conn,sql)


def load(db,table,schema,data,delete=True,batch_size=30000):
    if delete:
        sql = "drop table "+table
        try:
            exec(db,sql)
        except Exception as e:
            None
    
    sql = "create table `"+ table + "`("
    for c in schema:
        sql = sql + c + " " + schema[c] +","
    sql = sql[:-1] + ")" 
    try:
        exec(db,sql)
    except Exception as e:
        if "Object already exists" in e.args[1]:
            None
        else:
            print(e)
            return

    values = []
    total = 0
    for rows in data:
        total = total +1
        values.append("(" + ",".join(["\""+str(item).replace("\"","\\\"")+"\"" for item in rows]) + ")")
        if len(values) == batch_size or total == len(data):
            sql = "insert into `" + table + "` values "+ ",".join(values)
            try:
                exec(db,sql)
            except Exception as e:
                print(e)
            values = []
        
    print(table)




if __name__ == '__main__':
    c = conn("127.0.0.1",13303,"house")
    print(c)