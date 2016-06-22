# coding=utf8


# Sixth task definition
def do_task6():
    print '\n* Sixth task started...*\n'
    source_str = 'абвг'

    # Visual checking of input
    source_str_unicode = str(list(hex(ord(single_char)) for single_char in source_str))
    print 'Input string: \'%s\', in unicode (to visual checking purposes only): %s' % (source_str, source_str_unicode)

    # Calculate character code sum
    unicode_sum = sum(ord(single_char) for single_char in source_str)
    print 'Sum of unicode values: %d, in hex: %s' % (unicode_sum, hex(unicode_sum))

    print '\n*** Sixth task done...***'

# Auto execute section
if __name__ == '__main__':
    # Sixth task execution
    do_task6()
