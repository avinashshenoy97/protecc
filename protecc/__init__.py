__name__ = 'protecc'
__version__ = '0.0.1'

# =============== Imports =============== #
import inspect

# =============== Main =============== #
def __protecced_getattribute__(self, name: str, *args, **kwargs):
        if name.startswith('_'):
            varType = 'protected'
            if name.startswith('__'):
                varType = 'private'
                trailing = 0
                for s in name[::-1]:
                    if s == '_':
                        trailing += 1
                    if trailing > 1:
                        break
                if trailing <= 1:
                    name = '_' + self.__name__ + name
            try:
                if inspect.currentframe().f_back.f_locals['self'] is not self:
                    raise KeyError('self')
            except KeyError as ke:
                if str(ke) == "'self'":
                    raise AccessException('Cannot access ' + varType + ' member ' + name) from None

        if inspect.ismethod(name):
            return object.__getattribute__(self, name)(args, kwargs)
        else:
            return object.__getattribute__(self, name)

class metaProtecc(type):
    def __new__(cls, name, bases, dictspec):
        global __protecced_getattribute__
        ret = super().__new__(cls, name, bases, dictspec)
        ret.__getattribute__ = __protecced_getattribute__
        return ret

class protecc(metaclass=metaProtecc):
    pass


class AccessException(Exception):
    pass