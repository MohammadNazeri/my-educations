# Pydantic
Pydantic is a Python library designed to handle data validation and serialization efficiently by using type hints. It’s particularly useful when you want to enforce data types and constraints on your data, ensuring it adheres to specific formats and rules.

Core Concepts
1. Data Validation: Pydantic uses type hints to validate data. When you define a model with Pydantic, it will automatically check that the data you pass in conforms to the types you’ve specified.
2. Serialization and Deserialization: Pydantic can convert data between different formats. For example, it can serialize Python objects to JSON and deserialize JSON back to Python objects, ensuring the data conforms to the model.

## Data Validation Instruction 
* Defining Pydantic model:
```
  from pydantic import BaseModel, Field
  from typing import List, Optional

  class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: Optional[bool] = True
    tags: List[str] = []
```
  * Creating an instance of the User model by passing a dictionary that matches the model’s schema.
  ```
  user_data = {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "is_active": True,
    "tags": ["admin", "user"]
  }

  user = User(**user_data)
  print(user)
  ```
Pydantic performs automatic data validation. If the data doesn’t match the expected types, it will raise an error.

## Serialization and Deserialization
You can convert a Pydantic model instance to a dictionary or JSON format and vice versa.
```
# Convert to dictionary
user_dict = user.dict()
print(user_dict)

# Output:
# {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'is_active': True, 'tags': ['admin', 'user']}

# Convert to JSON
user_json = user.json()
print(user_json)

# Output:
# {"id": 1, "name": "Alice", "email": "alice@example.com", "is_active": true, "tags": ["admin", "user"]}
```
## Advanced Features > Custom Validators
In this example, the validate_email method ensures that the email address contains an @ symbol.
```
from pydantic import BaseModel, validator

class User(BaseModel):
    id: int
    name: str
    email: str

    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email address')
        return v
```
## BaseSettings
 It is used to handle settings from various sources, such as environment variables or configuration files (.env).
 ```
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    debug: bool = False
    database_url: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()
print(settings.app_name)

```
