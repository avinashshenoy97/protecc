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


def test_public_method_access():
    class regulatedClass(protecc):
        def foo(self):
            return 222

    obj = regulatedClass()
    assert obj.foo() == 222


def test_protected_method_access():
    class regulatedClass(protecc):
        def _foo(self):
            return 22

        def getProtectedB(self):
            return self._foo()

    obj = regulatedClass()
    with pytest.raises(AccessException):
        obj._foo()
    assert obj.getProtectedB() == 22


def test_private_method_access():
    class regulatedClass(protecc):
        def __foo(self):
            return 2

        def getPrivateB(self):
            return self.__foo()

    obj = regulatedClass()
    with pytest.raises(AccessException):
        obj.__foo()
    assert obj.getPrivateB() == 2


def test_public_static_method_access():
    class regulatedClass(protecc):
        def foo():
            return 222

    assert regulatedClass.foo() == 222
