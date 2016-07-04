import datetime as dt


# Definition of Order class
class Order(list):
    # Class'es fields
    '''
        # Instance fields:

        discount = 0
        total_price = 0.0
    '''
    # Common default value's fields
    date = dt.datetime.now()

    __total_orders = 0

    @classmethod
    def get_total_orders(cls):
        return Order.__total_orders

    def get_files(self):
        for e in (x for x in self if isinstance(x, DownloadableItem)):
            yield e

    def __new__(cls, *args, **kwargs):
        #print 'Instance of {} created'.format(cls)
        return super(Order, cls).__new__(cls, *args, **kwargs)

    def __init__(self, p_discount, *p_date):
        self._total_price = 0.0
        self._discount = p_discount
        if len(p_date) != 0:
            self.date = p_date[0]

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
                    '\n'.join(['\t\'{}\', {} pcs., ${};'.format(*x) for x in list(l_items)])
                    )

    @property
    def discount(self):
        return self._discount

    def __percent_discount(self, price):
        if self.discount == 0:
            return price
        else:
            return price - price *self.discount/100

    @discount.setter
    def discount(self, value):
        if 0 <= value < 100:
            self._discount = value
        else:
            raise ValueError('Discount should be in range [0..99]')

    '''
    @discount.deleter
    def discount(self):
        del self._discount
    '''

    @property
    def total_price(self):
        return self._total_price

    def append(self, p_object):
        if not isinstance(p_object, Item):
            raise TypeError('Only Item\'s type object can be added')
        else:
            self._total_price += self.__percent_discount(p_object.price)
            self.date = dt.datetime.now()
            Order.__total_orders += 1
        super(Order, self).append( p_object)

    def remove(self, p_object):
        if not isinstance(p_object, Item):
            raise TypeError('Only Item\'s type object cam be processed')
        else:
            self._total_price -= self.__percent_discount(p_object.price)
        super(Order, self).remove(p_object)


# Definition of Item class
class Item(object):
    # Item's fields
    id = 0
    name = '<name>'
    description = '<description>'
    price = 0.0

    def __init__(self, p_id, p_name, p_description, p_price):
        self.id = p_id
        self.name = p_name
        self.description = p_description
        self.price = p_price

    # String presentation of Items's objects
    def __str__(self):
        return 'Item; id: {}, name: \'{}\', description: \'{}\', price: {}'\
            .format(self.id , self.name, self.description, self.price)

    def __new__(cls, *args, **kwargs):
        #print 'Instance of ' + str(cls) + ' created...'
        return super(Item, cls).__new__(cls, *args, **kwargs)


# Definition of Downloadable Item class
class DownloadableItem(Item):
    filename = '<filename>'
    url = '<none>'
    downloads_count = 0

    def __init__(self, *arg):
        super(DownloadableItem, self).__init__(arg[0], arg[1], arg[2], arg[3])
        if (len(arg) > 4):
            self.filename = arg[4]
            self.url = arg[5]

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
    l_order.append(DownloadableItem(10, 'Manual', 'Lenovo ThinkPad T410', 5.60, 'Manual for notebook', 'http://lenovo.com/manuals/t410'))
    l_order.append(DownloadableItem(11, 'Book', 'Python for Dummy', 14.15, 'Safari\'s book', 'http://safari.com/books/pydummy'))
    l_order.append(DownloadableItem(12, 'Manual', 'Nokia E71', 2.00, 'Manual for mobile', 'http://lenovo.com/manuals/t410'))

    # View order content
    print '\nOrder: {},\nTotal items: {}\n'.format(l_order, l_order.get_total_orders())

    import random as rn
    for i in l_order.get_files():
        # Emulate multiple download to each Downloadable Item
        [f() for f in [i.get_url]*rn.randint(1, 20)]
        # Dispaly downloadable item
        print i
        print 'Html link: {}\n'.format(i.get_url())

# Second part
