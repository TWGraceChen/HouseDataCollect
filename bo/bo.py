import pymysql


def conn(host,port,db):
    db_settings = {
        "host": host,
        "port": port,
        "user": "root",
        "password": "",
        "db": db,
        "charset": "utf8"
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

if __name__ == '__main__':
    c = conn("127.0.0.1",13303,"house")
    print(c)