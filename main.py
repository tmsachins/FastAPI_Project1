from fastapi import FastAPI

# creating instance of the class
app = FastAPI()

@app.get('/')
def index():
    return 'Hello there!'

@app.get('/property/{id}')
def property(id:int):
    return (f'This is a property page for property {id}')

@app.get('/profile/{username}')
def profile(username:str):
    return (f'This is a profile page for user {username}')

@app.get('/movies')
def movies():
    return {'movie_list':{'Movie 1', 'Movie 2'}}


