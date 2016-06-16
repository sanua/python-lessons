# Third task definition
def do_task3():
    print '\n* Third task started...*\n'
    initSet = 'characterset'
    asSet = {v for v in initSet}
    testStr = 'Test String'
    for c in testStr:
        if c in asSet:
            print 'contain'
    print asSet
    print '\n*** Third task done...***'

# Auto execute section
if __name__ == '__main__':
    # Third task execution
    do_task3()
