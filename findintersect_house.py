from src import bo


l = [
    {"period":"108S3","table":["house_buy"],"city":["臺北市","新北市"]},
    {"period":"108S4","table":["house_buy"],"city":["臺北市","新北市"]},
    {"period":"109S1","table":["house_buy"],"city":["臺北市","新北市"]},
    {"period":"109S2","table":["house_buy"],"city":["臺北市","新北市"]}
    {"period":"109S3","table":["house_buy"],"city":["臺北市","新北市"]}
    {"period":"109S4","table":["house_buy"],"city":["臺北市","新北市"]}
]



for i in l:
    db = bo.conn("127.0.0.1",13303,i["period"])
    for t in i["table"]:
        print(i["period"]+"->"+t)
        where_stat = "where city in ('{}')".format("','".join(i["city"]))
        sql = '''update {0} a inner join 
            (select a.idx as idx,b.{3} as code from 
                (select *,1 as join from {2}) b 
            full inner join
                (select *,1 as join from {0} {1}) a 
            on a.join = b.join where ST_INTERSECTS(a.point,b.polygon)) b
            on a.idx = b.idx set {3} = b.code'''.format(t,where_stat,"house.area_code0","codebase")
        print(sql)
        bo.exec(db,sql)  
        sql = '''update {0} a inner join 
            (select a.idx as idx,b.{3} as code from 
                (select *,1 as join from {2}) b 
            full inner join
                (select *,1 as join from {0} {1}) a 
            on a.join = b.join where ST_INTERSECTS(a.point,b.polygon)) b
            on a.idx = b.idx set {3} = b.code'''.format(t,where_stat,"house.area_code1","code1")
        print(sql)
        bo.exec(db,sql)  
        sql = '''update {0} a inner join 
            (select a.idx as idx,b.{3} as code from 
                (select *,1 as join from {2}) b 
            full inner join
                (select *,1 as join from {0} {1}) a 
            on a.join = b.join where ST_INTERSECTS(a.point,b.polygon)) b
            on a.idx = b.idx set {3} = b.code'''.format(t,where_stat,"house.area_code2","code2")
        print(sql)
        bo.exec(db,sql)  
        sql = '''update {0} a inner join 
            (select a.idx as idx,b.{3} as code from 
                (select *,1 as join from {2}) b 
            full inner join
                (select *,1 as join from {0} {1}) a 
            on a.join = b.join where ST_INTERSECTS(a.point,b.polygon)) b
            on a.idx = b.idx set {3} = b.code'''.format(t,where_stat,"house.area_village","villcode")
        print(sql)
        bo.exec(db,sql)  
