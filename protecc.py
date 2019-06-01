# =============== Imports =============== #
import inspect

# =============== Main =============== #
class protecc:
    def __getattribute__(self, name: str, *args, **kwargs):
        if name.startswith('_'):
            varType = 'protected'
            if name.startswith('__'):
                varType = 'private'
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


class AccessException(Exception):
    pass