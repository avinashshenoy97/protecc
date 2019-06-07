# =============== Setup =============== #
import sys
import os

sys.path.append(os.path.abspath('../'))

# =============== Imports =============== #
from protecc import protecc, metaProtecc, AccessException


# =============== Main =============== #
class regulatedClass(protecc):
    def __init__(self):
        self.publicVariable = 'public value'
        self._protectedVariable = 'protected value'
        self._privateVariable = 'private value'

    def publicMethod(self):
        return True

    def _protectedMethod(self):
        return True

    def __privateMethod(self):
        return True

    def getProtectedVariable(self):
        return self._protectedVariable

    def getPrivateVariable(self):
        return self._privateVariable

    def protectedMethodProxy(self):
        return self._protectedMethod()

    def privateMethodProxy(self):
        return self.__privateMethod()

class metaRegulatedClass(regulatedClass, metaclass=metaProtecc):
    pass