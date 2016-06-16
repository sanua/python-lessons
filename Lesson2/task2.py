# Second task definition
def do_task2():
    print '\n* Second task started...*\n'
    foo(1, testFun)
    print '\n*** Second task done...***'

def testFun():
    return 'Function parameter'

def foo(*params):
    for p in params:
        if callable(p):
            print 'Parameter [', p, '] initialization: ', p()
        else:
            print 'Just a parameter: ', p

# Auto execute section
if __name__ == '__main__':
    # Second task execution
    do_task2()
