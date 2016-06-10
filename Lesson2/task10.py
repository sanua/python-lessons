# Tenth task definition
def doTask10():
    print '\n* Tenth task started...*\n'

    # Parse passed value
    parseResult = parseIntJSAnalog('1012100', 16)
    print 'Parsed string in specific base: %s' % parseResult

    print '\n*** Tenth task done...***'

# Parse function
def parseIntJSAnalog(stringValue, baseValue=10):
    result = 0
    value = int(stringValue)

    if baseValue == 2:
        # binary base
        result = '{0:b}'.format(value)
    elif baseValue == 8:
        # octal base
        baseValue = '{0:o}'.format(value)
    elif baseValue == 10:
        # decimal base
        result = '{0:d}'.format(value)
    elif baseValue == 16:
        # heximal base
        result = '{0:x}'.format(value)
    else:
        raise RuntimeError

    return result

# Auto execute section
if __name__ == '__main__':
    # Tenth task execution
    doTask10()
