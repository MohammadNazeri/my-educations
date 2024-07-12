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
```uvicorn main:app --reload```
