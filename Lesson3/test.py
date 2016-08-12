class MyClass(object):
    class_var = 1
    common_var = 10

    def __init__(self, i_var, *args, **kwargs):
        self.i_var = i_var
        if len(args) > 0:
            print 'args: ', args.__getitem__(len(args)-1)
        if (kwargs.get('common_var') != None):
            self.common_var = kwargs.get('common_var')


foo = MyClass(2, 120)
bar = MyClass(3, common_var = 112)

print foo.class_var, foo.i_var
print bar.class_var, bar.i_var
print MyClass.class_var

print MyClass.__dict__
try:
 print foo.__class__.__dict__['common_var']
except KeyError:
    print '-'
print foo.__dict__
#print foo.__dict__.__getattribute__('__doc__')
print foo.common_var
print bar.common_var

print '&&&'
print foo.common_var
setattr(MyClass, 'common_var', 500)
print foo.common_var


print '\n', MyClass.class_var
o = MyClass(100)
o.__class__.class_var
print o.class_var, MyClass.class_var


class BasePoint:
    '''
        # Instance object's attributes:
        point = (0, 0)
    '''

    def __init__(self, point):
        self.point = point

    def distance_to_origin(self):
        print 'Basepoint empty distance...', self.point


class CartezianPoint(BasePoint):

    def distance_to_origin(self):
        print 'Evaluate distance of cartezian point...', self.point
        # here evaluate distance for cortezian and return it


class ManhettenPoint(BasePoint):

    def distance_to_origin(self):
        print 'Evaluate distance of manhatten point...', self.point
        # evaluate of mathetten'sand return it


cp = (3, 4)
mp = (10, 20)

cp_object = CartezianPoint(cp)
mp_object = ManhettenPoint(mp)
print cp_object, mp_object
cp_object.distance_to_origin()
mp_object.distance_to_origin()


class NewtonPoint(ManhettenPoint):
    pass

np_object = NewtonPoint((100, 200));
np_object.distance_to_origin()

print '\n======================\n'

class Service():
    data = []
    def __init__(self, other_data):
        self.other_data = other_data
    def __str__(self):
        return 'Service instance: {}'.format(self.other_data)

s1 = Service(['a', 'b'])
s2 = Service(['c', 'd'])
s1.data = [1]
s2.data = [2]

print Service.data
print s1.data
print s2.data


