from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel,Field, computed_field
from typing import Annotated

# ---- validation model ----
class Person(BaseModel):
    id : Annotated[str, Field(...,description="id of person", examples="p1")]
    name: Annotated[str, Field(...,description="name of person")]
    age: Annotated[int,Field(...,gt=0,lt=100,description="age of person")]
    weight: Annotated[float,Field(...,gt=0,description="weight of person in kgs")]
    height: Annotated[float,Field(...,gt=0,description="weight of person in mts")]
    education: Annotated[str,Field(...,description="highest qualification of person")]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.height/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            verdict = "underweight"
        elif self.bmi <30:
            verdict = "normal"
        else:
            verdict = "obese"
        
        return verdict

# make instance of fastapi 
app = FastAPI()

# get data of people from people.json file
def get_people():
    with open('people.json','r') as f:
        content = json.load(f)
    return content

# save data of person from post request
def save_people(data):
    with open ('people.json', 'w') as f:
        json.dump(data,f)

# ----- get api -----
@app.get('/')
def hello():
    return {"greet":"hello api"}

@app.get('/about')
def about():
    return {"about":"this is my learning fast api series"}


# get info from database (in our case json file)
@app.get('/people')
def people():
    people = get_people()
    return people

# path parameter (if we want to find a specific person using id)
# path function helps readability of parameter. (... means its required or important)
@app.get('/person/{person_id}')
def person(person_id: str= Path(...,description="enter persons id",examples="p1")):
    person = get_people()

    if person_id in person:
        return person[person_id]
    else:
        raise HTTPException(status_code=404,detail='Person not found')
    
# query parameter (used to pass additional information to parameter , written as ?value&anothervalue)

@app.get('/sort')
def sort_people(sortby : str = Query(...,description="sort person based on age,weight"),order: str = Query('asc',description='sort in asc or desc order')):

    sort_index = ['age','weight']

    if sortby not in sort_index:
        raise  HTTPException(status_code=400,detail=f'invalid sortby value,select from {sort_index}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='invalid order value, select from asc or desc')
    
    person = get_people()
    orderby = True if order=='desc' else False
    sorted_data = sorted(person.values(),key=lambda x: x.get(sortby,0),reverse=orderby)

    return sorted_data

    # ------- post api -------

@app.post("/create")
def create_person(person: Person):
    # load existing data
    data = get_people()
        
    # check if person already exists
    if person.id in data:
        raise HTTPException(status_code=400,detail=f"person already exists")
        
    # add new person to database
    # -- since data is a dictionary and person is a pydantic object , we will first convert person into a dictionary
    data[person.id]= person.model_dump(exclude=['id'])

    save_people(data)

    return JSONResponse(status_code=201,content={"message":"person created successfuly"}) #201 means successful creation
