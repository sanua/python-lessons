# Seventh task definition
def doTask7():
    print '\n* Seventh task started...*\n'
    lists = [[1, 2, 3, 4],
             [2, 4, 4, 2],
             [6],
             [1, 1, 1, 1, 1]]
    print 'Source multi-dimension list: ', lists
    result = map(max, *lists)
    print 'The maximum values from  each list: %s' % result

    print '\n*** Seventh task done...***'

# Auto execute section
if __name__ == '__main__':
    # Seventh task execution
    doTask7()


