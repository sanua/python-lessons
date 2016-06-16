from task4 import INPUT_FILE_NAME as inFile
from task4 import outFile as printFile

# Fifth task definition
def do_task5():
    print '\n* Fifth task executed...*\n'
    # Output source file
    printFile(inFile, 'Source file:')
    # Read file
    readFile = file(inFile)
    lines = readFile.readlines()
    # Replace 'PHP' entries by the 'Python'
    result = [single_line.lower().replace('php', 'Python') for single_line in lines]
    print 'Replaced: \n%s' % result
    print '\n*** Fifth task done...***'

# Auto execute section
if __name__ == '__main__':
    # Fifth task execution
    do_task5()
