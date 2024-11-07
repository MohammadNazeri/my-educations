# Decorator
Use to add extra features to exsting function without changing the function.
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
