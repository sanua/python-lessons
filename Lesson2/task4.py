from os import remove as removeFile

# Define constants for file names
INPUT_FILE_NAME = 'task4.py'

OUTPUT_FILE_NAME = 'task4_reversed.py'

# This is testes section for task 5 which containt PHP entries
# PPH entry
# again PHP entry

# Fourth task definition
def doTask4():
    print '\n* Fourth task started...*\n'
    # Read file path
    # PycharmProjects/Python_Learning/Lesson2/task1.py
    #fName = raw_input('Input file name: ')
    fName = INPUT_FILE_NAME

    # Output file
    outFile(fName, 'Source file:')

    # Read from file
    readFile = file(fName, 'r')
    lines = readFile.readlines()
    readFile.close()

    # Reverse strings
    lines.reverse()

    # Write to file
    fName = OUTPUT_FILE_NAME
    writeFile = file(fName, 'w')
    writeFile.writelines(lines)
    writeFile.close()

    # Output file
    outFile(fName, 'Reversed file:')

    # Delete reverse file
    removeFile(fName)
    print '\n*** Fourth task done...***'

# Auxilary function to output file content on the screen
def outFile(fileName, *caption):
    if len(caption) > 0:
        print ' '.join(caption)
    fileToRead = file(fileName)
    lines = fileToRead.readlines()
    fileToRead.close()
    print '\tFile content:\n\t %s' % lines


# Auto execute section
if __name__ == '__main__':
    # Fourth task execution
    doTask4()
