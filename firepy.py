
from firebase_admin import credentials,initialize_app,db
import json

cred=credentials.Certificate("./fir-app.json")
app=initialize_app(cred,{
    'databaseURL':'https://fir-app-2fcd9-default-rtdb.firebaseio.com/'
    
})

ref =db.reference("/references/")

with open("./data1.csv","r") as f:
     data=json.load(f)
     
ref.set(data)
print("Database has been updated")
