# =============== Imports =============== #
import sys
import os

# =============== Setup =============== #
sys.path.append(os.path.abspath('../'))
import pytest
from protecc import protecc, AccessException

# =============== Main =============== #
@pytest.mark.run(order=1)
def test_import():
    assert protecc is not None


def test_public_data_access():
    class regulatedClass(protecc):
        def __init__(self):
            self.b = 222

    obj = regulatedClass()
    assert obj.b == 222


def test_protected_data_access():
    class regulatedClass(protecc):
        def __init__(self):
            self._b = 22

        def getProtectedB(self):
            return self._b

    obj = regulatedClass()
    with pytest.raises(AccessException):
        obj._b
    assert obj.getProtectedB() == 22


def test_private_data_access():
    class regulatedClass(protecc):
        def __init__(self):
            self.__b = 2

        def getPrivateB(self):
            return self.__b

    obj = regulatedClass()
    with pytest.raises(AccessException):
        obj.__b
    assert obj.getPrivateB() == 2