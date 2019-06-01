from protecc import protecc

class a(protecc):
    def foo(self, a, b=0):
        print('foo', a, b)
        self.a = a
        self.b = b
        return self.__bar()

    def __bar(self):
        print('bar')
        return 1