# First task definition
def do_task1():
    print '\n* First task started...*\n'
    print dir(__builtins__)
    print '\n*** First task done...***'

# Auto execute section
if __name__ == '__main__':
    #First task execution
    do_task1()