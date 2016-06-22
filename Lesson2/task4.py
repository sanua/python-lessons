from os import remove as remove_file

# Define constants for file names
INPUT_FILE_NAME = 'task4.py'

OUTPUT_FILE_NAME = 'task4_reversed.py'

# This is testes section for task 5 which containt PHP entries
# PPH entry
# again PHP entry


# Fourth task definition
def do_task4():
    print '\n* Fourth task started...*\n'
    # Read file path
    # PycharmProjects/Python_Learning/Lesson2/task1.py
    # f_name = raw_input('Input file name: ')
    f_name = INPUT_FILE_NAME

    # Output file
    out_file(f_name, 'Source file:')

    # Read from file
    read_file = open(f_name, 'r')
    lines = read_file.readlines()
    read_file.close()

    # Reverse strings
    lines.reverse()

    # Write to file
    f_name = OUTPUT_FILE_NAME
    write_file = open(f_name, 'w')
    write_file.writelines(lines)
    write_file.close()

    # Output file
    out_file(f_name, 'Reversed file:')

    # Delete reverse file
    remove_file(f_name)
    print '\n*** Fourth task done...***'


# Auxiliary function to output file content on the screen
def out_file(file_name, *caption):
    if len(caption) > 0:
        print ' '.join(caption)
    file_to_read = open(file_name)
    lines = file_to_read.readlines()
    file_to_read.close()
    print '\tFile content:\n\t %s' % lines


# Auto execute section
if __name__ == '__main__':
    # Fourth task execution
    do_task4()
