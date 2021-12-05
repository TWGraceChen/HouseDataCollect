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

]


#{"table":"hospital","area_table":"area_village","update_col" : "villcode","ref_col" : "villcode","key":"idx"},
for i in l:
    db = bo.conn("127.0.0.1",13303,"house")
    sql = '''update {0} a inner join 
        (select {4},b.{3} as code from 
            (select *,1 as join from {0}) a 
        full inner join
		    (select *,1 as join from {1}) b 
	    on a.join = b.join where ST_INTERSECTS(a.point,b.polygon)) b
        on a.{4} = b.{4} set {2} = b.code'''.format(i['table'],i['area_table'],i['update_col'],i['ref_col'],i['key'])
    print(sql)
    bo.exec(db,sql)    