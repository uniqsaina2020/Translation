from fastapi import FastAPI

app = FastAPI()


@app.get('/home/{name}/{age}')
def index(name:str, age:int, family:str='headar'):
    return {'massages': f'{name} {family} is {age} years old.'}

#http://127.0.0.1:8000/home/amir/20?family=ghasemi
#get max 2000 parametr & is not safe
#post safe and moust 2000 par

@app.post('/home/{name}/{age}')
def index(name:str, age:int, family:str='headar'):
    return {'massages': f'{name} {family} is {age} years old.'}