from task4 import INPUT_FILE_NAME as in_file


# Eighth task definition
def do_task8():
    print '\n* Eight task started...*\n'

    # Define file name to compile
    f_name = __file__
    # f_name = inFile

    res = ''
    # Compile specified file
    try:
        print 'Compiling module: \'%s\' ...' % f_name
        source_file = open(f_name, 'r')
        source_code = source_file.read()

        source_compiled = compile(source_code, '', 'exec')
    except Exception, e:
        print 'Compilation error: %s' % e.message
    else:
        print 'No errors'
    finally:
        source_file.close()

    print '\n*** Eight task done...***'


# Auto execute section
if __name__ == '__main__':
    # Eighth task execution
    do_task8()
