import datetime as dt

'''
Order *******************************************************************
'''
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

    def __new__(cls, *args, **kwargs):
        print 'Instance of {} created'.format(cls)
        return super(Order, cls).__new__(cls, *args, **kwargs)

    def __init__(self, p_discount, *p_date):
        self._total_price = 0.0
        self._discount = p_discount
        if p_date is not None:
            self.date = p_date

    # String presentation of Order's objects
    def __str__(self):
        import itertools as itl
        itl.cycle()
        return 'Order object; discount: {}, total price: {}, date: {}\nItems: {}'\
            .format(self.discount, self.total_price, self.date, list)

    @property
    def discount(self):
        return self._discount

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
            self._total_price += self.discount * p_object.price
        super(Order, self).append(p_object)

    def remove(self, p_object):
        if not isinstance(p_object, Item):
            raise TypeError('Only Item\'s type object cam be processed')
        else:
            self._total_price -= self.discount * p_object.price
        super(Order, self).remove(self, p_object)

'''
Item ********************************************************************
'''
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
        return 'Item object; id: {}, name: \'{}\', description: \'{}\', price: {}'\
            .format(self.id , self.name, self.description, self.price)

    def __new__(cls, *args, **kwargs):
        print 'Instance of ' + str(cls) + ' created...'
        return super(Item, cls).__new__(cls, *args, **kwargs)

'''
DownloadableItem ********************************************************
'''
# Definition of Downloadable Item class
class DownloadableItem(Item):
    filename = '<filename>'
    downloads_count = 0

    def __str__(self):
        return '\nDownloadableItem object; filename: {}, downloads_count: {}\n'\
            .format(self.filename, self.downloads_count)


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
    # First task execution

    l_order = Order(10)
    l_order.append(Item(1, 'Notebook', 'Asus notebook X202E', 345.50))
    l_order.append(Item(2, 'Phone', 'Apple smartpohone IPhone 6S', 975.00))
    l_order.append(Item(3, 'Camcoder', 'Panasonic mini DV camcode GS-500' , 925.10))
    l_order.append(Item(4, 'Notebook', 'Apple MacBook Pro 15"', 1450.80))
    l_order.append(Item(5, 'Phone', 'Nokia 3310', 7.50))
    l_order.append(Item(6, 'Camcoder', 'Cannon DV20', 800.50))
    l_order.append(Item(7, 'Notebook', 'Lenovo IdeaPad 100-15', 245.10))
    l_order.append(Item(8, 'Phone', 'Nokia E71', 145.00))
    l_order.append(Item(9, 'Notebook', 'Lenovo ThinkPad T410', 1400.00))

    print '\n'
    import itertools as it
    for key, item_group in it.groupby(l_order, lambda x: getattr(x, 'name')):
        #print key, item_group
        for item in item_group:
            print item.description, key
        print ' '

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]


