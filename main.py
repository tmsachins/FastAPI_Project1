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

class User(BaseModel):
    name: str
    email:str

# creating instance of the class
app = FastAPI()

@app.post('/purchase')
def purchase(user:User, product:Product):
    return {"user": user, "product": product}

@app.post('/addproduct/{product_id}')
def addproduct(product:Product,product_id: int, category:str):
    product.discounted_price = product.price - \
        (product.price * product.discount / 100)
    return {"product_id":product_id, "product": product, "category": category}

@app.post('/adduser')
def adduser(profile:Profile):
    return profile



