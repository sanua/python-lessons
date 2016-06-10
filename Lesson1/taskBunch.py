# coding=utf8
# import this
# import math
import math

#1
print "\n#1..."
print "Питон установлен. Ж%)"

#2
print "\n#2..."
multiple_result, lower_bound, upper_bound = 1, 1, 101
for i in range(lower_bound, upper_bound):
    multiple_result *= i
print 'Произведение чисел от 1 до 100:\t%10.10e' % (multiple_result)
print 'Произведение чисел от 1 до 100 (использование библиотеки math):\t %10.10e' % math.factorial(100)

#3
print "\n#3..."
string_array = [
    "Hello World!",
    "Hi pythonistas.",
    "Hello phpist and bye",
    "HELLO AND GOODBYE.",
    "Abracadabra",
    "Import antigravity",
]
print "Дан массив строк: %s" % string_array
current_a_count, letter_a_count, max_a_count_str, current_index, all_odd_strings, string_start_hello_bot_end_bye, sorted_strings = 0, 0, '', 0, [], [], ""
for p in string_array:
    # вычисление нечетных строк
    current_index += 1
    if current_index % 2 == 1:
        all_odd_strings.append(p)
    # поиск строк, начинающихся на 'Hello', но не заканчивающихся на 'bye'
    if p.lower().startswith('hello') and not p.lower().endswith('bye'):
        string_start_hello_bot_end_bye.append(p)
    # поиск строки с максимальным числом букв 'а'
    for i in p:
        if i.lower() == 'a':
            current_a_count += 1
    if current_a_count > letter_a_count:
        max_a_count_str = p
        letter_a_count = current_a_count
    current_a_count = 0;
#3.1
print "\t#3.1..."
print "\tСтрока с максимальным кол-вом букоф 'а': \"%s\", их колличество равно: %d" % (max_a_count_str, letter_a_count)
max_cnt_a, max_cnt_a_str = 0, ''
for s in string_array:
    current_cnt_a = 0
    current_cnt_a += s.count('a')
    current_cnt_a += s.count('A')
    if max_cnt_a < current_cnt_a:
        max_cnt_a = current_cnt_a
        max_cnt_a_str = s
print "\t(Версия2) Строка с максимальным кол-вом букоф 'а': \"%s\", их колличество равно: %d" % (max_cnt_a_str, max_cnt_a)
#3.2
print "\t#3.2..."
print "\tВсе нечетные строки: %s" % all_odd_strings
print "\t(Версия 2) Все нечетные строки: %s" % string_array[1::2]
#3.3
print "\t#3.3..."
print "\tСтроки начинающиеся на 'Hello', но не заканчивающиеся на 'bye': %s" % string_start_hello_bot_end_bye
result_strings = []
for s in string_array:
    s_lc = s.lower();
    if s_lc.startswith('hello') and not s_lc.endswith('bye'):
        result_strings.append(s)
print "\t(Версия 2) Строки начинающиеся на 'Hello', но не заканчивающиеся на 'bye': %s" % result_strings
#3.4
print "\t#3.4..."
sorted_strings = string_array[:]
sorted_strings.sort()
joined_strings = ""
for i in sorted_strings:
    joined_strings += i
print "\tОтсортированные: %s, \n\tи объединенные строки: \"%s\"" % (sorted_strings, joined_strings)
print "\t(Версия 2) Отсортированные: %s, \n\tи объединенные строки: \"%s\"" % (sorted(string_array), ''.join(sorted(string_array)))

# 4
print "\n#4..."
source_dict = {"q": 3, "w": 8, "e": "z", "r": "5", "t": 3}
print 'Дан словарь: %s' % source_dict
# 4.1
print "\t#4.1..."
swapper_key_values_dict = {}
for i in source_dict:
    swapper_key_values_dict[source_dict[i]] = i
print "\tПоменяные местами ключи и значения: %s" % swapper_key_values_dict
result_dict = dict()
for k, v in source_dict.items():
    if v not in result_dict:
        result_dict[v] = k
    else:
        if isinstance(result_dict[v], list):
            result_dict[v].append(k)
        else:
            new_list = []
            new_list.append(result_dict[v])
            result_dict[v] = new_list
            result_dict[v].append(k)
print "\t(Версия 2) Поменяные местами ключи и значения: %s" % result_dict
result_dict = {}
for k,v in source_dict.iteritems():
    result_dict[v] = result_dict.get(v, [])
    result_dict[v].append(k)
print "\t(Версия 3) Поменяные местами ключи и значения: %s" % result_dict

# 4.2
print "\t#4.2..."
from collections import OrderedDict as Order_Dict_Alias
swapper_key_values_dict = Order_Dict_Alias();
k = sorted(source_dict.keys())
for i in k:
    swapper_key_values_dict[i] = source_dict[i]
print "\tОтсортированные элементы по ключу: %s" % swapper_key_values_dict
#4.3
print "\t#4.3..."
chnaged_int_str_dict = source_dict.copy()
for p, r in swapper_key_values_dict.iteritems():
    if type(r) is str:
        chnaged_int_str_dict[p] += 'b'
    elif type(r) is int:
        chnaged_int_str_dict[p] += 1
    else:
        print type(r),
print "\tСловарь с увеличенными числами на 1 и добавленным к строкам 'b': %s" % chnaged_int_str_dict

#5
print "\n#5..."
transformed_flat_dict = {}
lower_bound_char = ord('a')
upper_bound_char = ord('z')
for i, j  in zip(list(range(1, (upper_bound_char - lower_bound_char) + 2)), list(range(lower_bound_char, upper_bound_char + 2))):
        transformed_flat_dict[chr(j)] = i
print "Словарь построенный из ключей - литер и значений - цифр: %s", transformed_flat_dict

#6
print "\n#6..."
top_bound_number = int(raw_input("Введите верхнюю границу выбора нахождения простых чисел: "))
print "Простые числа от 2 до %d:" % top_bound_number
# Function body
def find_simple_numbers(n):
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                print "\t%d равно %d * %d" % (i, j, i//j)
                break
        else:
            print "\t%d это простое число" % i
# End of function body
find_simple_numbers(top_bound_number)

#7
print "\n#7..."
arg1, arg2, arg3, arg4 = 10, 11, 23, 9
print "Аргументы функции: %s" % [arg1, arg2, arg3, arg4]
def sum_arguments(* multiple_arguments):
    arg_sum = 0
    for argument in multiple_arguments:
        arg_sum += argument
    return arg_sum
print "Сумма аргументов функции: %s" % sum_arguments(arg1, arg2, arg3, arg4)

#8
print "\n#8..."
input_dict = [1, 2, 3, 4, [4, 5, [6, 7]], 8]
print "Исходный словарь: %s" % input_dict
transformed_flat_dict = []
# Function body
def dict_2_flat(input_dict, result_dict):
    for element in input_dict:
        if isinstance(element,list):
            dict_2_flat(element, result_dict)
        else:
            result_dict.append(element)
    return result_dict
# End of function body
print "Плоский словарь: %s" % dict_2_flat(input_dict, transformed_flat_dict)