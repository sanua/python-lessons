from task4 import INPUT_FILE_NAME as in_file
from task4 import out_file as print_file


# Fifth task definition
def do_task5():
    print '\n* Fifth task executed...*\n'
    # Output source file
    print_file(in_file, 'Source file:')

    # Read file
    read_file = open(in_file)
    lines = read_file.readlines()

    # Replace 'PHP' entries by the 'Python'
    result = [single_line.lower().replace('php', 'Python') for single_line in lines]
    print 'Replaced: \n%s' % result
    print '\n*** Fifth task done...***'

# Auto execute section
if __name__ == '__main__':
    # Fifth task execution
    do_task5()
