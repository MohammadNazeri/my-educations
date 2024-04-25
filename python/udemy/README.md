# 100 Days of code
## Namespace
* Namespace is a context or scope in which identifiers (such as variables, functions, classes, etc.) are unique and can be used without conflicting with identifiers in other namespaces. 
* Scope defines the region of a program where a particular identifier can be accessed.There are three types of scopes:
  * Global scope: Variables defined outside of any function or class have global scope and can be accessed from anywhere within the program.
  * Local scope: Variables defined within a function or a block of code have local scope and are only accessible within that function or block.
  * Enclosing scope (non-local scope): In some programming languages like Python, nested functions can access variables defined in their enclosing function's scope. These variables are neither in the global nor local scope of the nested function but are accessible within it.
* Block scope: Unlike some other programming languages like C or JavaScript, Python does not have block-level scope for variables. It means when a variable is defined within the if or loop block, it is still accessible outside of the block.
### Modify global variable
* local and global variables
```
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")
```
* global variable and modify in a function
```
enemies = 1

def increase_enemies():
  global enemies
  enemies = 2
  print(f"enemies inside function: {enemies}")
```
## List/Dictionary comprehension
list comprehensions provide a concise way to create lists. They allow you to generate a new list by applying an expression to each item in an iterable.

```new_list = [expression for item in iterable if condition]```

```new_dic = {key_expression: value_expression for item in iterable if condition}```


## Error handling

```
try:
  [sth that might cause an exception]
except:
  [Do this if there was an exception]
else:
  [Do this if there was no exception]
finally:
  [always do this]
```
There are some kinds of Error types. They can be caught separately.
```
try:
  [sth that might cause an exception]
except FileNotFoundError:
  print("file not found")
except KeyError as error_messages:
  print("Key is not found")
  print(error_messages)
```
### Raise your own Exception
There are several different exceptions like SyntaxError, IndentationError, NameError, TypeError, ValueError, KeyError, IndexError, FileNotFoundError, ImportError and AttributeError.

```
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
```



* until 30
* 35 key authentication
* 36 stock trading
* 45-53-93 web scraping
* 46 spotify
* 47 amazon
* 48 selenium 
* 49 LinkedIn
* 50 Tinder
* 63 SQL
* 70 git
* 71 web application
* 72-81
* 92-99-100 data science
* 98 automation

