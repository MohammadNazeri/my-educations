# Test
Testing in Python is the process of checking whether your code behaves as expected
## Frameworks
### unittest
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
