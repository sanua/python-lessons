import datetime as dt
import math

import shlex

# Definition of Order class
from mercurial.hgweb.webutil import up


class Order(list):
    """Class instance fields:

        discount
        total_price
        date

    """
    __total_orders = 0

    @classmethod
    def get_total_orders(cls):
        return cls.__total_orders

    def get_files(self):
        for e in (x for x in self if isinstance(x, DownloadableItem)):
            yield e

    def __new__(cls, *args, **kwargs):
        cls.__total_orders += 1
        return super(Order, cls).__new__(cls, *args, **kwargs)

    def __init__(self, p_discount, p_date=None):
        self._total_price = 0.0
        self._discount = p_discount
        if p_date is not None:
            self.date = p_date
        else:
            self.date = dt.datetime.now()

    # String presentation of Order's objects
    def __str__(self):
        import itertools as itl

        l_items = (
            (key,
             len(list(group)),
             round(sum([x.price if (x.name == key) else 0 for x in self]), 2)
             )
                for key, group in
                   itl.groupby(
                       sorted(l_order, key=lambda x: x.name + str(x.id)),
                       key=lambda x: x.name
                   )
        )
        return 'Order\'s discount: {} %, amount: {} $, date: {}' \
               '\nItems:' \
               '\n{}'\
            .format(self.discount,
                    self.total_price,
                    self.date,
                    '\n'.join(['\t\'{}\', {} pcs., ${};'.format(*x) for x in l_items])
                    )

    @property
    def discount(self):
        return self._discount

    def __percent_discount(self, price):
        if self.discount == 0:
            return price
        else:
            return price - price * self.discount/100

    @discount.setter
    def discount(self, value):
        if 0 <= value < 100:
            self._discount = value
        else:
            raise ValueError('Discount should be in range [0..99]')

    @property
    def total_price(self):
        for it in self:
            if isinstance(it, Item):
                self._total_price += self.__percent_discount(it.price)
        return self._total_price

    def append(self, p_object):
        if not isinstance(p_object, Item):
            raise TypeError('Only Item\'s type object can be added')
        else:
            self.date = dt.datetime.now()
        super(Order, self).append( p_object)

    def remove(self, p_object):
        if not isinstance(p_object, Item):
            raise TypeError('Only Item\'s type object cam be processed')
        super(Order, self).remove(p_object)


# Definition of Item class
class Item(object):
    """Class instance fields

        id
        name
        description
        price
    """
    def __init__(self, p_id, p_name, p_description=None, p_price=0.0):
        self.id = p_id
        self.name = p_name
        self.description = p_description
        self.price = p_price

    # String presentation of Items's objects
    def __str__(self):
        return 'Item; id: {}, name: \'{}\', description: \'{}\', price: {}'\
            .format(self.id , self.name, self.description, self.price)

    def __new__(cls, *args, **kwargs):
        return super(Item, cls).__new__(cls, *args, **kwargs)


# Definition of Downloadable Item class
class DownloadableItem(Item):
    """Class instance fields

        filename
        url
        downloads_count
    """

    def __init__(self, p_id, p_name, p_description=None, p_price=0.0, p_file_name=None, p_url=None):
        super(DownloadableItem, self).__init__(p_id, p_name, p_description, p_price)
        self.filename = p_file_name
        self.url = p_url
        self.downloads_count = 0

    def __str__(self):
        return 'DownloadableItem; \n\t{},\n\tfilename: \'{}\', url: {}, downloads_count: \'{}\''\
            .format(super(DownloadableItem, self).__str__(), self.filename, self.url, self.downloads_count)

    def htmlize(*p_css_class):
        def parametrized_decorator(func):
            def wrapper_function(self, *args, **kwargs):
                # Invoke target function to increment count of downloads
                func(self, *args, **kwargs)

                l_css_class = None
                if len(p_css_class) > 0:
                    l_css_class = p_css_class[0]

                class_attr_str = ''
                if l_css_class is not None and len(str.strip(l_css_class)) > 0:
                    class_attr_str = 'class="{css_class}" '.format(css_class=l_css_class)

                return '<a {class_placeholder}href="{file_url}">{file_url}</a>'.format(file_url=self.url, class_placeholder=class_attr_str)
            return wrapper_function
        return parametrized_decorator

    @htmlize('test')
    def get_url(self):
        self.downloads_count += 1


# Some investigation of Python's MRO
class A(object):
    name = 'Object A'

    def __str__(self):
        return 'Object A; name: {}'.format(self.name)

    def do(self):
        print 'Do in A invoked'


class B(object):
    name = 'Object B'

    def __str__(self):
        return 'Object B; name: {}'.format(self.name)

    def do(self):
        super(B, self).do()
        print 'Do in B invoked'


class C(B, A):
    name = 'Object C'

    def __str__(self):
        return 'Object C; name: {}'.format(self.name)

    def __new__(cls, *args, **kwargs):
        print 'C instance ' + str(cls) + ' created'
        return super(C, cls).__new__(cls, *args, **kwargs)

    def do(self):
        super(C, self).do()
        print 'Do in C invoked'
# EoF some investigation of Python's MRO

# Auto execute section
if __name__ == '__main__':
# First part

    # Create an Order with 10% discount
    l_order = Order(10)

    # Add some items to order
    l_order.append(Item(1, 'Notebook', 'Asus notebook X202E', 345.50))
    l_order.append(Item(2, 'Phone', 'Apple smartpohone IPhone 6S', 975.00))
    l_order.append(Item(3, 'Camcoder', 'Panasonic mini DV camcode GS-500' , 925.10))
    l_order.append(Item(1, 'Notebook', 'Apple MacBook Pro 15"', 1450.80))
    l_order.append(Item(5, 'Phone', 'Nokia 3310', 7.50))
    l_order.append(Item(6, 'Camcoder', 'Cannon DV20', 800.50))
    l_order.append(Item(7, 'Notebook', 'Lenovo IdeaPad 100-15', 245.10))
    l_order.append(Item(8, 'Phone', 'Nokia E71', 145.00))
    l_order.append(Item(9, 'Notebook', 'Lenovo ThinkPad T410', 1400.00))

    # Add download item to order
    l_order.append(DownloadableItem(10, 'Manual', 'Lenovo ThinkPad T410', 5.60, 'Manual for notebook',
                                    'http://lenovo.com/manuals/t410'))
    l_order.append(DownloadableItem(11, 'Book', 'Python for Dummy', 14.15, 'Safari\'s book',
                                    'http://safari.com/books/pydummy'))
    l_order.append(DownloadableItem(12, 'Manual', 'Nokia E71', 2.00, 'Manual for mobile',
                                    'http://lenovo.com/manuals/t410'))

    # View order content
    print '\nOrder: {},\nTotal items: {}\n'.format(l_order, l_order.get_total_orders())

    import random as rn
    for i in l_order.get_files():
        # Emulate multiple download to each Downloadable Item
        for f in [i.get_url]*rn.randint(1, 20):
            f()
        # a = 10 if b() == c() else None

        # Dispaly downloadable item
        print i
        print 'Html link: {}\n'.format(i.get_url())

# Second part
print '\n'


# 2.1 definition
class CustomUniqueRandom(object):

    def __init__(self, p_lower_bound,  p_upper_bound):
        import random as rnd
        self._number_pool_set = set()
        self._lower_bound = p_lower_bound
        self._upper_bound = p_upper_bound
        self._number_pool_amount = p_upper_bound - p_lower_bound + 1
        self._count = 0

    def __iter__(self):
        return self

    def next(self):
        def generate_int():
            import random
            return random.randint(self._lower_bound, self._upper_bound)

        self._count += 1
        if self._count > self._number_pool_amount:
            raise StopIteration
        else:
            l_int = generate_int()
            while self._number_pool_set.__contains__(l_int) and len(self._number_pool_set) < self._number_pool_amount:
                l_int = generate_int()
            else:
                self._number_pool_set.add(l_int)

            if len(self._number_pool_set) == self._number_pool_set:
                raise StopIteration
            else:
                return l_int

# 2.1 result
ur = CustomUniqueRandom(10123, 10128)
for i in ur:
    print i,

# 2.2 definition
print '\n'


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
                raise StopIteration

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

gc = GeneratorClass(10, 17, 108)
print 'Generate numbers from {} to {}, till sum less than {}.'.format(gc.get_from, gc.get_to, gc.get_till)
for i in gc.generator():
    print i
print 'Current sum is {}.'.format(gc.get_amount)


# 2.3 definition
print '\n'
import functools as ft
import datetime as dt

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

print 'Source strings dates:\n\t{},\nConverted dates:\n\t{}'.format('\n\t'.join(l_date_strings), '\n\t'.join([str(e) for e in l_converted_dates]))