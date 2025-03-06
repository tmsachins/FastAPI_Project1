from fastapi import FastAPI
from pydantic import BaseModel
#pydantic allows us to create out own data types using models

class Profile(BaseModel):
    name: str
    email: str
    age: int

# creating instance of the class
app = FastAPI()

@app.post('/adduser')
def adduser(profile:Profile):
    return profile





# @app.get('/')
# def index():
#     return 'Hello there!'

# @app.get('/user/admin')
# def admin():
#     return (f'This is admin page')

# @app.get('/user/{username}')
# def profile(username:str):
#     return (f'This is a profile page for {username}')

# @app.get('/products')
# def products(id:int=None,price=None):
#     return {f'Product with an id: {id} and price {price}'}

# @app.get('/profile/{userid}/comments')
# def profile(userid:int,commentid:int):
#     return {f'Profile page for user with user id {userid} and comment with {commentid}'}



# @app.get('/movies')
# def movies():
#     return {'movie_list':{'Movie 1', 'Movie 2'}}


