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
