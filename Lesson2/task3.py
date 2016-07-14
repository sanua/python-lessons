# Third task definition
def do_task3():
    print '\n* Third task started...*\n'
    init_set = set('characterset')

    test_str = 'Test String'
    test_set = set(test_str)

    intersect_set = init_set.intersection(test_set)

    print 'Initial set: %s, have %d entries from the string: "%s"' % (init_set, len(intersect_set), test_str)
    print '\n*** Third task done...***'

# Auto execute section
if __name__ == '__main__':
    # Third task execution
    do_task3()
