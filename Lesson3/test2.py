def my_decorator(*top_args, **top_kwargs):
    def decorate_my_decorator(func):
        def fucking(*args, **kwargs):
            try:
                print 'Before call..'
                result = func(*args, **kwargs)
                print result
                return result
            finally:
                print top_args
                print top_kwargs
                print 'After call..'
        return fucking
    return decorate_my_decorator



@my_decorator(100, 'hi', first=1,second='twenty')
def add(a, b):
    return a + b


add(1, 3)

