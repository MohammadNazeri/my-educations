# Decorator
* In Python, a decorator is a design pattern that allows you to modify or enhance the behavior of a function or method without changing its actual code. It's a higher-order function, meaning it takes another function as an argument and returns a new function that typically extends or alters the behavior of the original function.
* Use to add extra features to exsting function without changing the function.
```
def div(a,b):
  print(a/b)

def smart_div(func):
  def inner(a,b):
    if a<b:
      a,b= b,a
    return func(a,b)
  return inner

div = smart_div(div)
div(2,4)
```
## The Decoration Process
When you apply a decorator using the @decorator_name syntax, what Python is really doing is replacing the decorated function with the new callable function returned by the decorator.
```
@my_decorator
def some_function():
    print("This is the original function.")
```
This is equivalent to:
```
def some_function():
    print("This is the original function.")

some_function = my_decorator(some_function)
```
Inside my_decorator, it returns a new function (the wrapper function), which is assigned back to some_function.

## The Role of the wrapper Function
The wrapper function is the new callable function that is created by the decorator. This function replaces the original some_function. When you call some_function(), you're actually calling the wrapper() function, not the original one. The wrapper() function then calls the original function (func()), often after adding behavior before or after the original function is executed.

## Decorators with Arguments
If you want to pass arguments to the decorated function, you need to adjust the wrapper to accept any number of arguments (and keyword arguments) using *args and **kwargs:
```
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function runs")
        result = func(*args, **kwargs)  # Call the wrapped function with arguments
        print("After the function runs")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(2, 3))  # Output: 5
```
## Built-in decorators
### @property
* In Python, the @property decorator is used to define methods that act like attributes.
* It allows you to define getter, setter, and deleter methods for an attribute
```
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

obj = MyClass(10)
print(obj.value)  # Calls the getter
obj.value = 20    # Calls the setter
```
