# Tenth task definition
def do_task10():
    print '\n* Tenth task started...*\n'

    l_string_value, l_base_value = '1012100', 8

    # Parse passed value
    for i in range(0, 100):
        parse_result = parse_int(l_string_value, i)
        print 'Parsed string: {0} in {1} base is: {2}'.format(l_string_value, i, parse_result)

    print '\n*** Tenth task done...***'


# Parse function
def parse_int(p_string, p_base=10):
    l_result, l_number = 0, 0
    try:
        l_number = int(p_string, p_base)
        l_result = '{0:d}'.format(l_number)

    except ValueError, e:
        l_result = None
        # print 'Conversion error: {0}\n'.format(e.message)

    return l_result

# Auto execute section
if __name__ == '__main__':
    # Tenth task execution
    do_task10()
