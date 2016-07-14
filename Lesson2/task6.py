# coding=utf8

# Sixth task definition
def doTask6():
    print '\n* Sixth task started...*\n'
    source_str = 'абвг'
    source_str_uncode = source_str.decode('utf8')

    # Visual checking of input
    print 'Input string: {}.\nInput string unicode: {}\n'.format(repr(source_str), repr(source_str_uncode))

    # Calculate character code sum
    unicodeSum = sum(ord(c) for c in source_str_uncode)
    print 'Sum of unicode values: %d' % unicodeSum

    print '\n*** Sixth task done...***'

# Auto execute section
if __name__ == '__main__':
    # Sixth task execution
    doTask6()