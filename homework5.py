immutable_var = (1, 2, True, False, 'String test', 3.0, ['1element str', '2_element str', 3])
print(immutable_var)
# immutable_var[1] = 9  - TypeError: 'tuple' object does not support item assignment

mutable_list = [1, 2, False, 4.0, 'String_str']
print(mutable_list)
mutable_list[2] = True
print(mutable_list)

immutable_var[6][1] = 'New_element_str'
print(immutable_var)
print(type(immutable_var))
print(type(mutable_list))
