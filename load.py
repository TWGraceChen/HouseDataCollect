from src import bo
import json
import busstation,carrefour,costco,eco,firestation,hospital,house,mrtstation,people,pharmarcy,park
import policestation,pxmart,rate,rtmart,school,shopseven,shopfamily,shophilife,shopokmart,simplemart,tymetrostation,shp
import airport,cleaninginstitution,cleaningteam,gas_station,incinerator,nuclear_powerplant,recyclablesdepot
import radio,factory,funeralfacilities,temple,ancestralhall,foundation,incineratorarea,incineratorchimney
import wastewater


path = "./data"
with open("schema.json") as f:
    schema = json.load(f)
db = bo.conn("127.0.0.1",13303,"house")


# busstation
data = busstation.Transform(path+'/busstation.csv')
table = "busstation"
bo.load(db,table,schema[table],data)

# carrefour
data = carrefour.Transform(path+'/carrefour.csv')
table = "carrefour"
bo.load(db,table,schema[table],data)  

# costco
data = costco.Transform(path+'/costco.csv')
table = "costco"
bo.load(db,table,schema[table],data)  


# eco
data = eco.Transform(path+'/eco.csv')
table = "eco"
bo.load(db,table,schema[table],data)  


# firestation
data1 = firestation.Transform1(path+'/firestation1.csv')
data2 = firestation.Transform2(path+'/firestation2.csv')
table = "firestation"
bo.load(db,table,schema[table],data1)   
bo.load(db,table,schema[table],data2,delete=False)  

# hospital
data = hospital.Transform(path+'/hospital.csv')
table = "hospital"
bo.load(db,table,schema[table],data)   

# mrtstation
data = mrtstation.Transform(path+'/mrtstation.csv')
table = "mrtstation"
bo.load(db,table,schema[table],data)   


# pharmarcy
data = pharmarcy.Transform(path+'/pharmarcy.csv')
table = "pharmarcy"
bo.load(db,table,schema[table],data)   


# policestation
data = policestation.Transform(path+'/policestation.csv')
table = "policestation"
bo.load(db,table,schema[table],data)   


# pxmart
data = pxmart.Transform(path+'/pxmart.csv')
table = "pxmart"
bo.load(db,table,schema[table],data)   


# rate
data = rate.Transform(path+'/rate.csv')
table = "rate"
bo.load(db,table,schema[table],data)   


# rtmart
data = rtmart.Transform(path+'/rtmart.csv')
table = "rtmart"
bo.load(db,table,schema[table],data)   


# shopfamily
data = shopfamily.Transform(path+'/shopfamily.csv')
table = "shopfamily"
bo.load(db,table,schema[table],data)   


# shophilife
data = shophilife.Transform(path+'/shophilife.csv')
table = "shophilife"
bo.load(db,table,schema[table],data)   

# shopokmart
data = shopokmart.Transform(path+'/shopokmart.csv')
table = "shopokmart"
bo.load(db,table,schema[table],data)   


# shopseven
data = shopseven.Transform(path+'/shopseven.csv')
table = "shopseven"
bo.load(db,table,schema[table],data)   

# simplemart
data = simplemart.Transform(path+'/simplemart.csv')
table = "simplemart"
bo.load(db,table,schema[table],data)   


# tymetrostation
data = tymetrostation.Transform(path+'/tymetrostation.csv')
table = "tymetrostation"
bo.load(db,table,schema[table],data)   

# people
data_base = people.Transform(path+'/people_base.csv')
data_1 = people.Transform(path+'/people_1.csv')
data_2 = people.Transform(path+'/people_2.csv')
table = "people_base"
bo.load(db,table,schema[table],data)   
table = "people_1"
bo.load(db,table,schema[table],data)  
table = "people_2"
bo.load(db,table,schema[table],data)  

# school
data = school.Transform(path+'/school')
table = "school"
bo.load(db,table,schema[table],data)   


# airport
data = tymetrostation.Transform(path+'/airport.csv')
table = "airport"
bo.load(db,table,schema[table],data) 

# cleaninginstitution
data = cleaninginstitution.Transform(path+'/cleaninginstitution.csv')
table = "cleaninginstitution"
bo.load(db,table,schema[table],data) 

# cleaningteam
data = cleaningteam.Transform(path+'/cleaninginstitution.csv')
table = "cleaningteam"
bo.load(db,table,schema[table],data) 


# gas_station
data = gas_station.Transform(path+'/gas_station.csv')
table = "gas_station"
bo.load(db,table,schema[table],data) 

# incinerator
data = incinerator.Transform(path+'/incinerator.csv')
table = "incinerator"
bo.load(db,table,schema[table],data) 

# nuclear_powerplant
data = nuclear_powerplant.Transform(path+'/nuclear_powerplant.csv')
table = "nuclear_powerplant"
bo.load(db,table,schema[table],data) 


# recyclablesdepot
data = recyclablesdepot.Transform(path+'/recyclablesdepot.csv')
table = "recyclablesdepot"
bo.load(db,table,schema[table],data) 


# radio
data = radio.Transform([path+'/am_radio.csv',path+'/fm_radio.csv'])
table = "radio"
bo.load(db,table,schema[table],data) 

# factory
data = factory.Transform(path+'/factory.csv')
table = "factory"
bo.load(db,table,schema[table],data) 

# park



# shp
#data0,data1,data2,datavillage = shp.Transform(path＋'/shp')
#table = "area_code0"
#bo.load(db,table,schema[table],data0,batch_size=100)    
#table = "area_code1"
#bo.load(db,table,schema[table],data1,batch_size=100)    
#table = "area_code2"
#bo.load(db,table,schema[table],data2,batch_size=100)    
#table = "area_village"
#bo.load(db,table,schema[table],datavillage,batch_size=100)  

    

# house
#for period in os.listdir(path＋'/house'):
#    data_a,data_b,data_c = house.Transform(path＋'/house/'+period,['a','b','c'])

#    db = bo.conn("127.0.0.1",13303,period)
#    with open("schema.json") as f:
#        schema = json.load(f)
#    table = "house_buy"
#    bo.load(db,table,schema[table],data_a) 
#    table = "house_pre_buy"
#    bo.load(db,table,schema[table],data_b)  
#    table = "house_rent"
#    bo.load(db,table,schema[table],data_c)    


# funeralfacilities
data = funeralfacilities.Transform(path+'/funeralfacilities.csv')
table = "funeralfacilities"
bo.load(db,table,schema[table],data) 

# temple
data = temple.Transform(path+'/temple.csv')
table = "temple"
bo.load(db,table,schema[table],data) 

# ancestralhall
data = ancestralhall.Transform(path+'/ancestralhall.csv')
table = "ancestralhall"
bo.load(db,table,schema[table],data) 


# foundation
data = foundation.Transform(path+'/foundation.csv')
table = "foundation"
bo.load(db,table,schema[table],data) 

# incineratorarea
data = incineratorarea.Transform(path+'/incineratorarea.csv')
table = "incineratorarea"
bo.load(db,table,schema[table],data) 

# incineratorchimney
data = incineratorchimney.Transform(path+'/incineratorchimney.csv')
table = "incineratorchimney"
bo.load(db,table,schema[table],data) 


# wastewater
data = wastewater.Transform(path+'/wastewater.csv')
table = "wastewater"
bo.load(db,table,schema[table],data) 