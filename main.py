from fastapi import FastAPI
from pydantic import BaseModel
#pydantic allows us to create out own data types using models

class Profile(BaseModel):
    name: str
    email: str
    age: int

class Product(BaseModel):
    name: str
    price: int
    discount:int
    discounted_price: float

# creating instance of the class
app = FastAPI()

@app.post('/addproduct')
def addproduct(product:Product):
    product.discounted_price = product.price - \
        (product.price * product.discount / 100)
    return product

@app.post('/adduser')
def adduser(profile:Profile):
    return profile



