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
# Data structure
* ### list
   * It is built-in data structure in Python
   * my_list = [1, 2, 3, 'a', 'b', 'c']
   * It is mutable (changable values)
   * It can contain elements of different data types.
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
      *
      ```
      name = 'Alice'
      age = 30
      print("Name: %s, Age: %d" % (name, age))
      print("Name: {}, Age: {}".format(name, age))
      print(f"Name: {name}, Age: {age}")
      ```
