my_dict = {'Alex' : 1948, 'Vlad' : 1947, 'Diana' : 2000, 'Ben': 2019}
print (my_dict)
print(my_dict.get('Vlad'))
my_dict['Arina'] = 2009
print(my_dict['Arina'])
my_dict.update({'Vasia' : 2017, 'Petia' : 2015})
a = my_dict.pop('Vlad')
print(a)
print(my_dict)
print(' ')
print('Множества')
print('')
my_set = {1, 2, 3, 1, 2, 3, (1, 4, 7), (1, 4, 7), 'Admin', True, 'Admin', True}
print(my_set)
my_set.update({5, False})
print(my_set)
my_set.remove(2)
print(my_set)