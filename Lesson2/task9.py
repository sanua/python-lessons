# Ninth task definition
def doTask9():
    print '\n* Ninth task started...*\n'

    sumOfArgs = argSumFunction(1, 2, 3, 100, [200, 300, 400, [1,2,3,1]], (1000, 2000,), {10000, 20000})
    print 'Sum of arguments: ', sumOfArgs

    print '\n*** Ninth task done...***'

def argSumFunction(*args):
    #================ Auxilary function to process lists ================
    def listSum(listArg):
        # Check if function has arguments
        if (len(args)) == 0:
            return 0

        internalSum = 0
        for e in listArg:
            if isinstance(e, list) or isinstance(e, tuple) or isinstance(e, set):
                internalSum += listSum(e)
            else:
                internalSum += e
        else:
            return internalSum
    #=====================================================================

    # Check if function has arguments
    if (len(args)) == 0:
        return 0

    # Evaluate sum
    sumResult = 0
    for single_arg in args:
        if isinstance(single_arg, int):
            sumResult += single_arg
        elif isinstance(single_arg, list) or isinstance(single_arg, tuple) or isinstance(single_arg, set):
            sumResult += listSum(single_arg)
        else:
            raise TypeError

    # return resuklt
    return sumResult

# Auto execute section
if __name__ == '__main__':
    # Ninth task execution
    doTask9()
