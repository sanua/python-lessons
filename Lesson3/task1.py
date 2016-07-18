import datetime as dt
import random as rn
import itertools as itl


class Order(list):
    """ Class instance fields:
            discount
            total_price
            date
    """

    # Class attribute to store orders amount
    __total_orders = 0

    def __init__(self, p_discount, p_date=None):
        self._total_price = 0.0
        self._discount = p_discount
        if p_date is not None:
            self.date = p_date
        else:
            self.date = dt.datetime.now()

    def __new__(cls, *args, **kwargs):
        cls.__total_orders += 1
        return super(Order, cls).__new__(cls, *args, **kwargs)

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

    # String presentation of Order's objects
    def __repr__(self):
        l_items = (
            (key,
             len(list(group)),
             round(sum([x.price if (x.name == key) else 0 for x in self]), 2)
             )
                for key, group in
                   itl.groupby(
                       sorted(self, key=lambda x: x.name + str(x.id)),
                       key=lambda x: x.name
                   )
        )
        return 'Order\'s discount: {} %, amount: {} $, date: {}' \
               '\nItems:' \
               '\n{}' \
               '\n\tTotal items:{}' \
               '\nTotal orders:{}'\
            .format(self.discount,
                    self.total_price,
                    self.date,
                    '\n'.join(['\t\'{}\', {} pcs., ${};'.format(*x) for x in l_items]) if (len(self) > 0) else '\t{}'.format(None),
                    len(self),
                    self.get_total_orders()
                    )

    @property
    def discount(self):
        return self._discount

    @property
    def total_price(self):
        for it in self:
            if isinstance(it, Item):
                self._total_price += self.__percent_discount(it.price)
        return self._total_price

    @classmethod
    def get_total_orders(cls):
        return cls.__total_orders

    @discount.setter
    def discount(self, value):
        if 0 <= value < 100:
            self._discount = value
        else:
            raise ValueError('Discount should be in range [0..99]')

    def __percent_discount(self, price):
        if self.discount == 0:
            return price
        else:
            return price - price * self.discount/100

    def get_files(self):
        for e in (x for x in self if isinstance(x, DownloadableItem)):
            yield e


# Definition of Item class
class Item(object):
    """ Class instance fields:
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

    def __new__(cls, *args, **kwargs):
        return super(Item, cls).__new__(cls, *args, **kwargs)

    # String presentation of Items's objects
    def __repr__(self):
        return 'Item; id: {}, name: \'{}\', description: \'{}\', price: {}'\
            .format(self.id , self.name, self.description, self.price)


# Definition of Downloadable Item class
class DownloadableItem(Item):
    """ Class instance fields:
            filename
            url
            downloads_count
    """

    def __init__(self, p_id, p_name, p_description=None, p_price=0.0, p_file_name=None, p_url=None):
        super(DownloadableItem, self).__init__(p_id, p_name, p_description, p_price)
        self.filename = p_file_name
        self.url = p_url
        self.downloads_count = 0

    def __repr__(self):
        return 'DownloadableItem; \n\t{},\n\tfilename: \'{}\', url: {}, downloads_count: \'{}\''\
            .format(super(DownloadableItem, self).__repr__(), self.filename, self.url, self.downloads_count)

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


# ******************** Some investigation of Python's MRO ********************
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
# ******************** EoF some investigation of Python's MRO ********************

# Auto execute section
if __name__ == '__main__':

    # Create an Order with 10% discount
    first_order = Order(10)

    # Add some items to order
    first_order.append(Item(1, 'Notebook', 'Asus notebook X202E', 345.50))
    first_order.append(Item(2, 'Phone', 'Apple smartpohone IPhone 6S', 975.00))
    first_order.append(Item(3, 'Camcoder', 'Panasonic mini DV camcode GS-500', 925.10))
    first_order.append(Item(1, 'Notebook', 'Apple MacBook Pro 15"', 1450.80))
    first_order.append(Item(5, 'Phone', 'Nokia 3310', 7.50))
    first_order.append(Item(6, 'Camcoder', 'Cannon DV20', 800.50))
    first_order.append(Item(7, 'Notebook', 'Lenovo IdeaPad 100-15', 245.10))
    first_order.append(Item(8, 'Phone', 'Nokia E71', 145.00))
    first_order.append(Item(9, 'Notebook', 'Lenovo ThinkPad T410', 1400.00))

    # Add download item to order
    first_order.append(DownloadableItem(10, 'Manual', 'Lenovo ThinkPad T410', 5.60, 'Manual for notebook',
                                    'http://lenovo.com/manuals/t410'))
    first_order.append(DownloadableItem(11, 'Book', 'Python for Dummy', 14.15, 'Safari\'s book',
                                    'http://safari.com/books/pydummy'))
    first_order.append(DownloadableItem(12, 'Manual', 'Nokia E71', 2.00, 'Manual for mobile',
                                    'http://lenovo.com/manuals/t410'))

    # View order content
    print '\nOrder: {}\n'.format(first_order, first_order.__len__())

    # Second order
    second_order = Order(99)
    print '{}\n'.format(second_order)

    for i in first_order.get_files():
        # Emulate multiple download to each Downloadable Item
        for f in [i.get_url]*rn.randint(1, 20):
            f()
        # a = 10 if b() == c() else None

        # Dispaly downloadable item
        print i
        print 'Html link: {}\n'.format(i.get_url())