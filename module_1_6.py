my_dict = {'Alexander' : 1999, 'Boris' : 1997, 'Vladimir' : 1989}
print(my_dict)
print(my_dict['Boris'])
print(my_dict.get('Valery'))
my_dict.update({'Valery' : 1991,
                'Daria' : 1995})
reserve = my_dict.pop('Alexander')
print(reserve)
print(my_dict)

my_set = {'String_1', 2, 1, 2, 3, 4, 4, 5, 6, 7, 77, 7, 'String_1'}
print(my_set)
my_set.add(33), my_set.add(41)
print(my_set)
my_set.remove(4)
print(my_set)