from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl

# creating instance of the class
app = FastAPI()

def receive_signal(signalNumber, frame):
    print('Received:', signalNumber)
    sys.exit()


@app.on_event("startup")
async def startup_event():
    import signal
    signal.signal(signal.SIGINT, receive_signal)

# ---------------

#pydantic allows us to create out own data types using models
from typing import Set

class Profile(BaseModel):
    name: str
    email: str
    age: int

class Image(BaseModel):
    url:HttpUrl
    name:str

class Product(BaseModel):
    name: str
    price: int = Field(title="Price of the item",gt=0, description = "This would be the price of the item being added")
    discount:int
    discounted_price: float
    tags: Set[str] = []
    image: Image

class User(BaseModel):
    name: str
    email:str


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



