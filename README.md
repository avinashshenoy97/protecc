# protecc
Access modifiers for python.


## Setup

#### PIP install [WIP]

```bash
pip install protecc
```

#### From the source [WIP]

```bash
git clone https://github.com/avinashshenoy97/protecc
cd protecc
python setup.py install
```

## Usage

### Old-Style Classes
Inherit from/extend the `protecc` class.

```python
from protecc import protecc

class regulatedClass(protecc):
    def __init__(self):
        self.publicVariable = 'public value'
        self._privateVariable = 'private value'

    def publicMethod(self):
        return True

    def __privateMethod(self):
        return True

    def getPrivateVariable(self):
        return self._privateVariable

    def privateMethodProxy(self):
        return self.__privateMethod()
```

### New-Style Classes (type)
 
If you prefer metaclass (for better readability/what not), use `metaProtecc`.

```python
class metaRegulatedClass(metaclass=metaProtecc):
    def __init__(self):
        self.publicVariable = 'public value'
        self._privateVariable = 'private value'

    def publicMethod(self):
        return True

    def __privateMethod(self):
        return True

    def getPrivateVariable(self):
        return self._privateVariable

    def privateMethodProxy(self):
        return self.__privateMethod()
```

When accessing "private" methods (i.e, methods that begin with either a single or two underscores), this exception is raised

```python
>>> r = regulatedClass()
>>> r.__privateMethod()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/avinashshenoy/STUFF/projects/protecc/protecc.py", line 23, in __protecced_getattribute__
    raise AccessException('Cannot access ' + varType + ' member ' + name) from None
protecc.AccessException: Cannot access private member __privateMethod
```

Private methods can still be accessed from within other class methods, as is expected:

```python
>>> r = regulatedClass()
>>> r.privateMethodProxy()
True
```

### Note

- This is, by no means, fool-proof access protection.
- "Private members" are those members whose names are mangled by Python, as per PEP 8 conventions, i.e, starting with 2 underscores and having not more than one trailing underscore.
- Additionally, "protected members" are those members whose names are preceded by a single underscores. These members cannot be accessed from outside the class as well, as is expected.

## Primary Contributors

| | |
|:-:|:-:|
|<img src="https://github.com/avinashshenoy97.png" width="48">  | [Avinash Shenoy](https://github.com/avinashshenoy97) |

#### License

This project is released under the [MIT License](https://github.com/avinashshenoy97/protecc/blob/master/LICENSE).