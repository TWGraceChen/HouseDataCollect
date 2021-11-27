from src import bo
import json
import busstation,carrefour,costco,eco,firestation,hospital,house,mrtstation,people,pharmarcy,park
import policestation,pxmart,rate,rtmart,school,shopseven,shopfamily,shophilife,shopokmart,simplemart,tymetrostation




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


# house
# park
# people
# school