from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


names = ["faraal", "Sadoon", "raid", "orhaan"]




#-----------------------------------------------------------------------------------
@app.get("/") 
def get_function(): 
    return names  

#-----------------------------------------------------------------------------------

class Data(BaseModel):
    name: str
   
   
# create
@app.post("/") # url
def post_function(data: Data):
    names.append(data.name)
    return names
    
#-----------------------------------------------------------------------------------

@app.delete("/{name}") #url
def delete_data(name: str):
    names.remove(name)
    return names 
    
#-----------------------------------------------------------------------------------

@app.put("/{name}")
def update_data(name: str, data: Data):
    for i, n in enumerate(names):
        if n == name:
            names[i] = data.name
    return names
