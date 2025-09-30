# Test
Testing in Python is the process of checking whether your code behaves as expected
## Frameworks
### unittest — The Built-in Testing Framework
Structure:
* Test cases are written as classes that inherit from unittest.TestCase.
* Assertions are made with special assertion methods.
```
import unittest

def multiply(a, b):
    return a * b

class TestMath(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 10), 0)

if __name__ == '__main__':
    unittest.main()
```
### pytest — Third-party Framework, Very Popular
Structure:
* Tests are just regular Python functions (no need to use classes).
* Uses standard Python assert statements.
* Test discovery is automatic for files named like test_*.py.
* pip install pytest
```
def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 10) == 0
```

# Mock
mock refers to a technique (and a library) used primarily for unit testing. It allows you to replace parts of your system under test with mock objects and make assertions about how they were used.
### mock
Mock is a class that can simulate (mock) any object. You can specify return values, assert calls, and more.
```
from unittest.mock import Mock

# Create a mock object
my_mock = Mock()

# Simulate a method call
my_mock.some_method.return_value = 10

# Call the method
result = my_mock.some_method()

print(result)  # Output: 10
print(my_mock.some_method.called)  # True
```
### MagicMock
MagicMock is a subclass of Mock that has default implementations of Python magic methods (like __len__, __getitem__, etc.).
Use MagicMock when you need to mock objects that rely on special methods like __len__, __getitem__, etc.
```
from unittest.mock import MagicMock

# Create a MagicMock object
my_magic = MagicMock()

# Use magic methods
print(len(my_magic))  # Works, returns another Mock object by default

# You can also set a return value for __len__
my_magic.__len__.return_value = 5
print(len(my_magic))  # Output: 5
```
### patch
patch is a context manager and decorator used to temporarily replace an object in a module with a mock.
```
# math_ops.py
def get_data():
    return [1, 2, 3]

def process_data():
    data = get_data()
    return sum(data)
```
We want to test process_data without relying on get_data.
#### Example 1: Patch as a context manager
```
from unittest.mock import patch
import math_ops

with patch('math_ops.get_data') as mocked_get_data:
    mocked_get_data.return_value = [10, 20, 30]
    result = math_ops.process_data()
    print(result)  # Output: 60
```
#### Example 2: Patch as a decorator
```
@patch('math_ops.get_data')
def test_process_data(mocked_get_data):
    mocked_get_data.return_value = [5, 5]
    result = math_ops.process_data()
    assert result == 10
```
#### patch & mock 
* Mock() creates a mock object — it's like saying “Here’s a fake thing.”
* patch() temporarily replaces a real thing with a fake thing (a mock) — usually to replace something imported from another module.
