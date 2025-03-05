from fastapi import FastAPI

# creating instance of the class
app = FastAPI()

@app.get('/')
def index():
    return 'Hello there!'

@app.get('/property')
def property():
    return 'This is a property page'

@app.get('/movies')
def movies():
    return {'movie_list':{'Movie 1', 'Movie 2'}}


