from fastapi import FastAPI, Path, HTTPException, Query
import json

# make instance of fastapi 
app = FastAPI()

# get data of people from people.json file
def get_people():
    with open('people.json','r') as f:
        content = json.load(f)
    return content

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
def person(person_id: str= Path(...,description="enter persons id",example="p1")):
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