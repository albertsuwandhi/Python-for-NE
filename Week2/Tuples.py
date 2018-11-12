#!/usr/bin/env python3
# Tuples are immutables
my_tuple = (1, 'whatever',0.5)
print("Type of my_tuples : ", type(my_tuple))
for i in my_tuple:
    print(i)
#convert tuples to list
my_list = list(my_tuple)
print("Type of my_list : ", type(my_list))
for i in my_list:
    print(i)
#list element can be changed
my_list[0] = 100




