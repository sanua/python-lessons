from task4 import INPUT_FILE_NAME as inFile
import py_compile

# Eighth task definition
def doTask8():
    print '\n* Eigth task started...*\n'

    # Define file name to compile
    fName = __file__
    #fName = inFile

    # Compile specified file
    try:
        print 'Compiling module: \'%s\' ...' % fName
        res = py_compile.compile(fName)
    except Exception, e:
        res = str(e)

    # Write compilation result
    if res == None:
        print 'No errors'
    else:
        print res

    '''
        TODO: Seems that therte is no way to catching compilation errors, even in different external module... it's so pity (
    '''

    print '\n*** Eigth task done...***'

# Auto execute section
if __name__ == '__main__':
    # Eighth task execution
    doTask8()
