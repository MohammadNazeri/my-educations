   # Python
## Elementary
```
age = input("please enter your age")
age = int(age)
```
```
if (5>4) and (a==6):  
   print("sth")  
elif (a%2):
   print("sth else")  
else:  
   print("else")
```
```
import math   
math.sin(0.6)
or
from math import sin
sin(0.6)
```
```
def func(str):
   print(str)
func("salam")
```
```
def sum(a,b):
   return a+b
s = sum(1,2)
```
```
friends = ['a', 'b', 'c']
for friend in friends:
   print(friend)
```
## Data structure
* ### list
   * It is built-in data structure in Python
   * my_list = [1, 2, 3, 'a', 'b', 'c']
   * It is mutable (changable values)
   * It can contain elements of different data types.
* ### Tuple
   * tuple is a collection data type similar to a list. However, unlike lists, tuples are immutable.
   * my_tuple = (1, 2, 3, 'a', 'b', 'c')
   * Packing and Unpacking   
      ```
      my_tuple = a, b, c  # Packing
      x, y, z = my_tuple  # Unpacking
      ```
* ### array
   * It can only contain elements of the same data type.
   *  my_array = array.array('i', [1, 2, 3, 4, 5])
   *  Arrays are using the array function, specifying the type code and the initial values.
   *  my_array = array.array('i', [1, 2, 3, 4, 5])
   *  'i' denotes the type code for signed integers.
*  ### dictionary
   * Dictionaries are mutable, unordered collections of items. Each item in a dictionary consists of a key-value pair, where the key must be unique and immutable, while the value can be of any data type and mutable.
   *  my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
*  ### String
   * my_string = 'Hello, world!'
   * Strings are immutable.
      *  my_string[0] = 'J' ERROR
      *  new_string = "J" + my_string[1:] created new string.
      * string formatting
      ```
      name = 'Alice'
      age = 30
      print("Name: %s, Age: %d" % (name, age))
      print("Name: {}, Age: {}".format(name, age))
      print(f"Name: {name}, Age: {age}")
      ```
## Files
* Using Context Managers (with Statement): It automatically handles opening and closing the file, even if an error occurs within the block.
  ```
  with open('example.txt', 'r') as file:
    content = file.read()
  // File is automatically closed when exiting the `with` block
  ```
* Error Handling: This is often done using try and except blocks.
  ```
  try:
    file = open('example.txt', 'r')
    content = file.read()
  except FileNotFoundError:
     print("File not found")
  finally:
     file.close()  # Ensure the file is closed even if an error occurs
   ```
## lambda
* myfunc = lambda x: x*2
* myfunc(2)
* a.sort(lambda x:x[1]) > sort based on second element of each array

### map
* Applies a specified function to all the items in an iterable (like a list, tuple, etc.)
* map(function, iterable, ...)
* list(map(lambda x:x*2, iterable))
* list(map(lambda x:'big if x>10 else 'small', iterable))
### filter
* It constructs an iterator from elements of an iterable (like a list, tuple, etc.) for which a specified function returns true.
* filter(function, iterable)
* list(filter(lambda x: x%2==0, iterable)

## generator
* a generator is a special type of iterable, which generates values on the fly instead of storing them in memory all at once.
* Generators are defined using a function containing one or more yield statements.
```
def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1
```
* The yield statement pauses the function's execution and saves its state so that it can resume from that point when called again.

## OOP
* A class defines the attributes (data) and methods (functions) that the objects will have.
* An object is an instance of a class.
* "self" is a convention used within methods of a class to refer to the instance of the class itself. It is the first parameter of any method in a class, though you don't need to pass it explicitly when calling the method.
* __init__ is a constructor method and __del__ is distructor method.
```
class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count = Person.count + 1
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
   def __del__(self):
         Person.count = Person.count - 1

person1 = Person("Alice", 30)
person1.greet()
```
* "count" is a class variable. It is used like "Person.count" (not self.count). name and age are object variables. All objects can see class variables but the opposite is not true.
### inheritance
* Inheritance is a mechanism in which a new class (subclass) can inherit attributes and methods from an existing class (superclass).
```
class Student(Person):  # Student class inherits from Person
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # Call the superclass constructor
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying hard for the exam.")

# Creating instances of Person and Student classes
person1 = Person("Alice", 30)
student1 = Student("Bob", 25, "A")
```
* Extension: Subclasses can extend the functionality of their superclass(es) by adding new attributes and methods.
* Overriding: Subclasses can override methods of their superclass(es) to provide their own implementation e.g. __init__ method.
* super().__init__ calls constructor of superclass.

* 
## Context manager (with statement)
## Virtual Environment
A Python virtual environment (venv) is simply a directory (project directory) with a particular file structure. It has a bin subdirectory that includes links to a Python interpreter as well as subdirectories that hold packages installed in the specific venv. 
* follow commands should be run on project directory(Linux).
```
python -m venv [name] > creates directory with [name]
python -m venv env
source env/bin/activate > To activate the environment
pip list
pip install [package name]
pip freeze > requirement.txt > To get all packages and versions to give to others
pip install -r requirements.txt > install all packages in new env
deactivate > To deactivate the environment
```

