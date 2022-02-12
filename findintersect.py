from src import bo


l = [
    {"table":"carrefour","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"carrefour","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"carrefour","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"carrefour","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    {"table":"costco","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"costco","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"costco","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"costco","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    {"table":"firestation","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"firestation","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"firestation","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"firestation","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    {"table":"mrtstation","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"mrtstation","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"mrtstation","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"mrtstation","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    {"table":"pharmarcy","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    {"table":"policestation","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"policestation","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"policestation","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"policestation","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    {"table":"pxmart","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"pxmart","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"pxmart","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"pxmart","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
        {"table":"tymetrostation","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"tymetrostation","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"tymetrostation","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"tymetrostation","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    
    {"table":"shopseven","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"shopseven","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"shopseven","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"shopseven","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    
    {"table":"shopfamily","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"shopfamily","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"shopfamily","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"shopfamily","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},

    {"table":"shopokmart","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    {"table":"shophilife","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    {"table":"simplemart","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    {"table":"rtmart","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},

    {"table":"hospital","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    {"table":"school","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    {"table":"airport","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    {"table":"incinerator","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    {"table":"cleaningteam","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    
    {"table":"cleaninginstitution","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    {"table":"recyclablesdepot","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    

    {"table":"radio","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"radio","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"radio","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"radio","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    
    {"table":"nuclear_powerplant","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},

    {"table":"gas_station","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"gas_station","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"gas_station","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"gas_station","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},

    {"table":"funeralfacilities","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},  

    {"table":"temple","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"temple","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"temple","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"temple","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},

    {"table":"ancestralhall","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"ancestralhall","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"ancestralhall","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"ancestralhall","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},

    {"table":"foundation","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"foundation","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"foundation","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"foundation","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},

    {"table":"incineratorarea","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},  
    
    {"table":"incineratorchimney","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"incineratorchimney","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"incineratorchimney","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"incineratorchimney","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    {"table":"wastewater","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"wastewater","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"wastewater","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"wastewater","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
    {"table":"waste","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},  
    {"table":"nightmarket","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},  
     {"table":"powerplant","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},  
    {"table":"lpg","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"}, 

    {"table":"busstation","area_table":"area_code2","update_col":"code2","ref_col":"code2","key":"idx"},
    {"table":"busstation","area_table":"area_code1","update_col":"code1","ref_col":"code1","key":"idx"},
    {"table":"busstation","area_table":"area_code0","update_col":"codebase","ref_col":"codebase","key":"idx"},
    {"table":"busstation","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
]




batch = 1000
db = bo.conn("127.0.0.1",13303,"house")
for i in l:
    print(i['table']+"->"+i['update_col'])
    result = bo.query(db,"select count(*) from "+i['table'])
    total = result[0][0]
    finish = 0
    to = 0
    last = False
    while not last:
        to = batch
        if finish + batch >= total:
            to = total - finish
            last = True
        sql = '''update {0} a inner join 
            (select a.{4} as {4},b.{3} as code from 
                (select *,1 as join from {1}) b 
            full inner join
                (select *,1 as join from {0} limit {5},{6}) a 
	        on a.join = b.join where ST_INTERSECTS(a.point,b.polygon)) b
            on a.{4} = b.{4} set {2} = b.code'''.format(i['table'],i['area_table'],i['update_col'],i['ref_col'],i['key'],finish,to)
        
        #print(sql)
        bo.exec(db,sql)  
        finish = finish + to  