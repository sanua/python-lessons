# Ninth task definition
def do_task9():
    print '\n* Ninth task started...*\n'

    # sum_of_ags = number_and_collection_arg_sum_function(1, 2, 3, 100, [200, 300, 400, [1, 2, 3, 1]], (1000, 2000,), {10000, 20000})
    sum_of_ags = number_arg_sum_function(1, 2, 3, 100, )
    print 'Sum of arguments: ', sum_of_ags

    print '\n*** Ninth task done...***'


def number_and_collection_arg_sum_function(*args):
    # ================ Auxiliary function to process lists ================
    def list_sum(list_arg):
        # Check if function has arguments
        if (len(args)) == 0:
            return 0

        internal_sum = 0
        for e in list_arg:
            if isinstance(e, list) or isinstance(e, tuple) or isinstance(e, set):
                internal_sum += list_sum(e)
            else:
                internal_sum += e
        else:
            return internal_sum
    # =====================================================================

    # Check if function has arguments
    if (len(args)) == 0:
        return 0

    # Evaluate sum
    sum_result = 0
    for single_arg in args:
        if isinstance(single_arg, int):
            sum_result += single_arg
        elif isinstance(single_arg, list) or isinstance(single_arg, tuple) or isinstance(single_arg, set):
            sum_result += list_sum(single_arg)
        else:
            raise TypeError

    return sum_result

def number_arg_sum_function(*args):
    # Check if function has arguments
    if (len(args)) == 0:
        return 0

    # Evaluate sum
    sum_result = 0
    for single_arg in args:
        if isinstance(single_arg, int):
            sum_result += single_arg
        else:
            raise TypeError('Only numbers allowed')

    return sum_result


# Auto execute section
if __name__ == '__main__':
    # Ninth task execution
    do_task9()
