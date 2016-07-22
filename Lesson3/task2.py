import functools as ft
import datetime as dt
import random as rn

# 2.1 definition
class CustomUniqueRandom(object):

    def __init__(self, p_lower_bound,  p_upper_bound):
        self._number_pool_set = set()
        self._lower_bound = p_lower_bound
        self._upper_bound = p_upper_bound
        self._number_pool_amount = p_upper_bound - p_lower_bound + 1
        self._count = 0

    def __iter__(self):
        return self

    def next(self):
        def generate_int():
            return rn.randint(self._lower_bound, self._upper_bound)

        self._count += 1
        if self._count > self._number_pool_amount:
            raise StopIteration
        else:
            l_int = generate_int()
            while l_int in self._number_pool_set and len(self._number_pool_set) < self._number_pool_amount:
                l_int = generate_int()
            else:
                self._number_pool_set.add(l_int)

            if len(self._number_pool_set) == self._number_pool_set:
                raise StopIteration
            else:
                return l_int

# 2.1 result
l_lower_gen, l_upper_gen = 10123, 10128
print 'Generated elements from {} to {} i random order:'.format(l_lower_gen, l_upper_gen)
ur = CustomUniqueRandom(l_lower_gen, l_upper_gen)
print '\t',
for i in ur:
    print i,

# 2.2 definition
class GeneratorClass(object):
    def __init__(self, p_number_lower_bound, p_number_upper_bound, p_bound_sum):
        # Internal fields
        self._range = range(p_number_lower_bound, p_number_upper_bound + 1)
        self._current_sum = 0

        # Initialized fields
        self._number_lower_bound = p_number_lower_bound
        self._number_upper_bound = p_number_upper_bound
        self._bound_sum = p_bound_sum

    def generator(self):
        for i in self._range:
            if self._current_sum + i < self._bound_sum:
                self._current_sum += i
                yield i
            else:
                return

    @property
    def get_from(self):
        return self._number_lower_bound

    @property
    def get_to(self):
        return self._number_upper_bound

    @property
    def get_till(self):
        return self._bound_sum

    @property
    def get_amount(self):
        return self._current_sum

# 2.2 result
gc = GeneratorClass(10, 17, 108)
print '\n\nGenerate numbers from {} to {}, till sum less than {}.'.format(gc.get_from, gc.get_to, gc.get_till)
print '\t',
for i in gc.generator():
    print i,
print '\nCurrent sum is {}.'.format(gc.get_amount)

# 2.3 definition
l_date_strings = ["12 Jan 1989",
                  "13 Feb 1990",
                  "14 Mar 1991",
                  "15 Apr 1992",
                  "16 May 1993",
                  "16 Jun 1994"]


def parse_date(*args, **kwargs):
    return dt.datetime.strptime(args[1], args[0])

l_converted_dates = map(
    ft.partial(parse_date, '%d %b %Y'),
    l_date_strings
)

# 2.3 result
print '\nSource strings dates:\n\t{},\nConverted dates:\n\t{}'.format('\n\t'.join(l_date_strings), '\n\t'.join([str(e) for e in l_converted_dates]))