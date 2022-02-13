
from src import function as func
from src import bo

conf = [
    {"result":"unified.codebase","area_table":"area_code0","count":"codebase","type":"char(13)"},
    {"result":"unified.code1","area_table":"area_code1","count":"code1","type":"char(12)"},
    {"result":"unified.code2","area_table":"area_code2","count":"code2","type":"char(8)"},
    {"result":"unified.villcode","area_table":"area_village","count":"villcode","type":"char(11)"}
]

resource = [
    'airport',
    'ancestralhall',
    'busstation',
    'carrefour',
    'cleaninginstitution',
    'cleaningteam',
    'costco',
    'firestation',
    'foundation',
    'funeralfacilities',
    'gas_station',
    'hospital',
    'incinerator',
    'incineratorarea',
    'incineratorchimney',
    'lpg',
    'mrtstation',
    'nightmarket',
    'nuclear_powerplant',
    'pharmarcy',
    'policestation',
    'powerplant',
    'pxmart',
    'radio',
    'recyclablesdepot',
    'rtmart',
    'school',
    'shopfamily',
    'shophilife',
    'shopokmart',
    'shopseven',
    'simplemart',
    'temple',
    'tymetrostation',
    'waste',
    'wastewater'
]





db = bo.conn("127.0.0.1",13303,"house")
for c in conf:
    print("==="+c["result"]+"===")
    # prepare create statment
    create_stat = "create table {} ({} {}".format(c["result"],c["count"],c["type"])
    for r in resource:
        create_stat = "{},{} int64".format(create_stat,r)
    
    
    # create table
    ws = c["result"].split(".")[0]
    sql = "create database "+ws
    try:
        bo.exec(db,sql)
    except Exception as e:
        print(sql)
        print(e)

    sql = "drop table "+c["result"]
    try:
        bo.exec(db,sql)
    except Exception as e:
        print(sql)
        print(e) 
    sql = create_stat+")"  
    try:
        bo.exec(db,sql)
    except Exception as e:
        print(sql)
        print(e)
    
    # insert area id
    sql = "insert into {0} ({1}) select {1} from {2}".format(c["result"],c["count"],c["area_table"])
    try:
        bo.exec(db,sql)
    except Exception as e:
        print(sql)
        print(e)

    # update count column
    for r in resource:
        sql = '''update {0} a inner join
        (select {1},count(*) as cnt from {2} group by {1}) b 
        on a.{1} = b.{1} set {2} = b.cnt
        '''.format(c["result"],c["count"],r)
        try:
            bo.exec(db,sql)
        except Exception as e: 
            print(sql)
            print(e)
        

    

