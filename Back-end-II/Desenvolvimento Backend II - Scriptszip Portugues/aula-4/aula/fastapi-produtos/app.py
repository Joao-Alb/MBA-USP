from fastapi import FastAPI
from models.product import Product

app = FastAPI()

@app.get('/')
def hello_world():
    """
    Frist Endpoint to say hello world
    """
    return {"Hello":"World!"}

@app.get('/{nome}')
def hello(nome: str):
    if not nome:
        pass
    return {"Hello":nome}


data = [
    Product(id=1,name="Tenis Nike Air", description="Otimo calçado", price=199.99),
    Product(id=2,name="Iphone", description="Celulares", price=1999.99),
    Product(id=3,name="Samsung", description="Celulares", price=1989.99),
    Product(id=4,name="Notebook", description="Eletrônicos", price=4989.99),
]

@app.get("/api/products")
def get_products():
    return data

@app.get("/api/products/{id}")
def get_products_by_id(id: int):
    for product in data:
        if product.id == id:
            return product
    return {"message":"Product Not found in DB"}