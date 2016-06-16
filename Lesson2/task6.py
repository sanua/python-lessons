
# Sixth task definition
def do_task6():
    print '\n* Sixth task started...*\n'
    sourceStr = u'\u0430\u0431\u0432\u0433'

    # Visual checking of input
    sourceStringInCharacter = sourceStr.encode('utf-8')
    sourceStringInUnicode = str(list(hex(ord(singleChar)) for singleChar in sourceStr))
    print 'Input string: \'%s\', in unicode (to visual checking purposes only): %s' % (sourceStringInCharacter, sourceStringInUnicode)

    # Calculate character code sum
    unicodeSum = sum(ord(single_char) for single_char in sourceStr)
    print 'Sum of unicode values: %d' % unicodeSum

    print '\n*** Sixth task done...***'

# Auto execute section
if __name__ == '__main__':
    # Sixth task execution
    do_task6()