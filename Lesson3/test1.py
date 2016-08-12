class A(object):
    def __init__(self, p_f1, p_f2):
        self._f1 = p_f1
        self._f2 = p_f2

    @property
    def f1(self):
        return self._f1

    @property
    def f2(self):
        return self._f2

    @f1.setter
    def f1(self, value):
        if (value >= 0) and (value < 100):
            self._f1 = value
        else:
            raise ValueError('Value should be between 0 and 99')

    @f1.deleter
    def f1(self):
        del self._f1

    def __str__(self):
        return 'Instance of  A class:\n\tf1: \'{}\'\n\tf2: \'{}\''.format(self.f1, self.f2)


print '\n===============================\n'
l_a = A(0, 'q')
print l_a
l_a.f1 = 10
print l_a