# FastAPI
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.  
How to use it:  
``` pip install fastapi ```
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```
Uvicorn is an ASGI server implementation commonly used with FastAPI (Asynchronous Server Gateway Interface).

```uvicorn main:app --reload```

Uvicorn will run the API on http://localhost:8000.

### Features 
* Path Parameters
  ```
  @app.get("/greet/{name}") 
  def greet(name: str): 
    return f"Hello {name}"
    ```
* Query Parameters
  ```
  @app.get("/items/")
  def read_items(category: str, brand: str): 
    ...
    ```
* Request Body  
  The request body contains the data in a request, for example, in a POST request.  
    ```
    from pydantic import BaseModel
    
    class Item(BaseModel):
        name: str
        description: str
        price: float
    
    @app.post("/items/")
    def create_item(item: Item):
        ...
    ```
* Response Model
  ```
  from pydantic import BaseModel

  class Item(BaseModel):
    name: str
    description: str 
    price: float

  @app.get("/items/")
  def read_items():
    items = [Item(name="Foo", description="A new item", price=45.2), 
             Item(name="Bar", description="Another item", price=10.5)]
    return items
    ```
* Authentication
    ```
    @app.get("/protected")
    def proteceted(password: str, required_password="secret"):
    if password == required_password:
        return "Success!"
    return "Invalid password"
    ```
    ```
    @app.get("/protected")
    def protected(authorization: str):
    if authorization == "token 12345":
        return "Success!"
    return "Invalid token"
    ```
* Testing
  ```
  from fastapi.testclient import TestClient

    client = TestClient(app)

    def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
    ```
