from src import bo


l = [
    {"period":"108S3","table":["house_buy"],"city":["臺北市","新北市"]},
    {"period":"108S4","table":["house_buy"],"city":["臺北市","新北市"]},
    {"period":"109S1","table":["house_buy"],"city":["臺北市","新北市"]},
    {"period":"109S2","table":["house_buy"],"city":["臺北市","新北市"]},
    {"period":"109S3","table":["house_buy"],"city":["臺北市","新北市"]},
    {"period":"109S4","table":["house_buy"],"city":["臺北市","新北市"]}
]


batch = 1000
for i in l:
    db = bo.conn("127.0.0.1",13303,i["period"])
    for t in i["table"]:
        print(i["period"]+"->"+t)
        result = bo.query(db,"select count(*) from "+t)
        total = result[0][0]
        finish = 0
        to = 0
        last = False
        where_stat = "where city in ('{}')".format("','".join(i["city"]))
        while not last:
            to = batch
            if finish + batch >= total:
                to = total - finish
                last = True
        
            sql = '''update {0} a inner join 
                (select a.idx as idx,b.{3} as code from 
                    (select *,1 as join from {2}) b 
                full inner join
                    (select * from (select *,1 as join from {0} limit {4},{5}) {1}) a 
                on a.join = b.join where ST_INTERSECTS(a.point,b.polygon)) b
                on a.idx = b.idx set {3} = b.code'''.format(t,where_stat,"house.area_code0","codebase",finish,to)
            #print(sql)
            bo.exec(db,sql)  
            sql = '''update {0} a inner join 
                (select a.idx as idx,b.{3} as code from 
                    (select *,1 as join from {2}) b 
                full inner join
                    (select * from (select *,1 as join from {0} limit {4},{5}) {1}) a 
                on a.join = b.join where ST_INTERSECTS(a.point,b.polygon)) b
                on a.idx = b.idx set {3} = b.code'''.format(t,where_stat,"house.area_code1","code1",finish,to)
            #print(sql)
            bo.exec(db,sql)  
            sql = '''update {0} a inner join 
                (select a.idx as idx,b.{3} as code from 
                    (select *,1 as join from {2}) b 
                full inner join
                    (select * from (select *,1 as join from {0} limit {4},{5}) {1}) a 
                on a.join = b.join where ST_INTERSECTS(a.point,b.polygon)) b
                on a.idx = b.idx set {3} = b.code'''.format(t,where_stat,"house.area_code2","code2",finish,to)
            #print(sql)
            bo.exec(db,sql)  
            sql = '''update {0} a inner join 
                (select a.idx as idx,b.{3} as code from 
                    (select *,1 as join from {2}) b 
                full inner join
                    (select * from (select *,1 as join from {0} limit {4},{5}) {1}) a 
                on a.join = b.join where ST_INTERSECTS(a.point,b.polygon)) b
                on a.idx = b.idx set {3} = b.code'''.format(t,where_stat,"house.area_village","villcode",finish,to)
            #print(sql)
            bo.exec(db,sql) 
            finish = finish + to   
            print(finish)
