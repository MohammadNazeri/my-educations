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
#### patch & mock 
* Use Mock when you want to make your own fake object.
* Use patch when you want to replace something that already exists in your code.

### MagicMock
* MagicMock is a subclass of Mock 
* Unlike Mock, MagicMock has default implementations of Python magic methods (like __len__, __iter__, __add__ etc.).
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
#### Mock & MagicMock
When to use which?
* Use Mock for simple objects (methods, attributes).
* Use MagicMock when:
    * The object is iterated over
    * You're mocking objects used with with statements
    * Operators (+, in, comparisons) need to work
    * You want fewer manual definitions
## @pytest.fixture
A fixture is a reusable function that provides a fixed baseline or setup that your tests can use.
* Set up resources before a test runs
* Tear down resources after the test (if needed)
* Inject data or objects into tests automatically via dependency injection
```
import pytest

@pytest.fixture
def sample_data():
    return {"x": 1, "y": 2}

def test_sum(sample_data):
    assert sample_data["x"] + sample_data["y"] == 3
```
Key features:
* Automatic injection: pytest matches fixture names to test function parameters.
* Scope control: You can run fixtures per test, per module, per session, etc.
    * E.g. Fixture is created once per test class. All test methods in the class share the same fixture instance.
  ```@pytest.fixture(scope="module")```
* Teardown using yield:
```
@pytest.fixture
def resource():
    conn = open_resource()
    yield conn
    conn.close()
```
## @pytest.mark.asyncio
