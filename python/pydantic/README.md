# Pydantic
Pydantic is a Python library designed to handle data validation and serialization efficiently by using type hints. It’s particularly useful when you want to enforce data types and constraints on your data, ensuring it adheres to specific formats and rules.

Core Concepts
1. Data Validation: Pydantic uses type hints to validate data. When you define a model with Pydantic, it will automatically check that the data you pass in conforms to the types you’ve specified.
2. Serialization and Deserialization: Pydantic can convert data between different formats. For example, it can serialize Python objects to JSON and deserialize JSON back to Python objects, ensuring the data conforms to the model.

## Instruction
* Defining Pydantic model:
'''
  from pydantic import BaseModel, Field
  from typing import List, Optional

  class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: Optional[bool] = True
    tags: List[str] = []
'''
  * Creating an instance of the User model by passing a dictionary that matches the model’s schema.
  '''
  user_data = {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "is_active": True,
    "tags": ["admin", "user"]
  }

  user = User(**user_data)
  print(user)
  '''
