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


def test_public_data_access():
    for objectFactory in (regulatedClass, metaRegulatedClass):
        obj = objectFactory()
        assert obj.publicVariable == 'public value'


def test_protected_data_access():
    for objectFactory in (regulatedClass, metaRegulatedClass):
        obj = objectFactory()
        with pytest.raises(AccessException):
            obj._protectedVariable
        assert obj.getProtectedVariable() == 'protected value'


def test_private_data_access():
    for objectFactory in (regulatedClass, metaRegulatedClass):
        obj = objectFactory()
        with pytest.raises(AccessException):
            obj.__privateVariable
        assert obj.getPrivateVariable() == 'private value'
