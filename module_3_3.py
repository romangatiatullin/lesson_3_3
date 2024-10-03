def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(10)
print_params(10, 'буква')
print_params(15, 'число', False)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = (False, [1,2,3], 'элемент')
values_dict = {'a':12.3 ,'b':None, 'c':'словарь'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = (123, 'скибиди')
print_params(*values_list_2,42)