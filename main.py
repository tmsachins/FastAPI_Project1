from fastapi import FastAPI

# creating instance of the class
app = FastAPI()

@app.get('/')
def index():
    return 'Hello there!'

@app.get('/user/admin')
def admin():
    return (f'This is admin page')

@app.get('/user/{username}')
def profile(username:str):
    return (f'This is a profile page for {username}')

@app.get('/products')
def products(id:int=1,price=0):
    return {f'Product with an id: {id} and price {price}'}



# @app.get('/movies')
# def movies():
#     return {'movie_list':{'Movie 1', 'Movie 2'}}


