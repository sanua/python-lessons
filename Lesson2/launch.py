# Import all defined modules
'''
from task1 import do_task1 as f1
from task2 import do_task2 as f2
from task3 import do_task3 as f3
from task4 import do_task4 as f4
from task5 import do_task5 as f5
from task6 import do_task6 as f6
from task7 import do_task7 as f7
from task8 import do_task8 as f8
from task9 import do_task9 as f9
from task10 import do_task10 as f10
'''

# Import modules name space
from sys import modules

# Iterate ovel all the modules and execute tasks
C_MODULE_NAME_TEMPLATE = 'task'
C_FUNCTION_NAME_TEMPLATE = 'do_task'

for l_order in range(1, 11):
    # Prepare module
    l_mod_name = C_MODULE_NAME_TEMPLATE + str(l_order)
    __import__(l_mod_name)
    l_mod = modules[l_mod_name]
    print 'Module name: %s, module: %s' % (l_mod_name, l_mod)

    # Get function from module
    l_func_name = C_FUNCTION_NAME_TEMPLATE + str(l_order)
    l_func = getattr(l_mod, l_func_name)
    print 'Function name: %s, function: %s' % (l_func_name, l_func)

    # Execute function
    l_func()

# Execute all defined modules
'''
# Run task 1
do_task1()

# Run task 2
do_task2()

# Run task 3
do_task3()

# Run task 4
do_task4()

# Run task 5
do_task5()

# Run task 6
do_task6()

# Run task 7
do_task7()

# Run task 8
do_task8()

# Run task 9
do_task9()

# Run task 10
do_task10()

'''