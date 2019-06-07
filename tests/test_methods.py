# =============== Setup =============== #
import sys
import os

sys.path.append(os.path.abspath('../'))


# =============== Imports =============== #
import pytest

from common import *
from protecc import AccessException


# =============== Main =============== #
@pytest.mark.run(order=1)
def test_import():
    assert protecc is not None


def test_public_method_access():
    for objectFactory in (regulatedClass, metaRegulatedClass):
        obj = objectFactory()
        assert obj.publicMethod()


def test_protected_method_access():
    for objectFactory in (regulatedClass, metaRegulatedClass):
        obj = objectFactory()
        with pytest.raises(AccessException):
            obj._protectedMethod()
        assert obj.protectedMethodProxy()


def test_private_method_access():
    for objectFactory in (regulatedClass, metaRegulatedClass):
        obj = objectFactory()
        with pytest.raises(AccessException):
            obj.__privateMethod()
        assert obj.privateMethodProxy()
