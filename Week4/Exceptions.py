#!/usr/bin/env python3

my_dict = {'brand':'cisco'}
'''
print("BEFORE")
print(my_dict['model'])
'''
try:
    print("BEFORE")
    print(my_dict['model'])
    print("AFTER")
except KeyError:
    print("--- Caught Exception -----")
    #raise 
print("--After Exception--")
print("-"*40)

try:
    print(my_dict['model'])
except KeyError as e:
    print(e.__class__)
    print(str(e))
    print("--- Caught Exception : Print Info ---")
print("-"*40)

my_list=[]
try:
    print(my_list[1])
    print(my_dict['model'])
except (KeyError,IndexError):
    print("Multiple Exception handled")
print("-"*40)

try:
    print(my_list[1])
    print(my_dict['model'])
except KeyError:
    print("Key Error Exception")
except IndexError:
    print("Index Error Exception")
print("-"*80)

try:
    print(my_dict['model'])
except Exception as e:
    print(e.__class__)
    print(str(e))
    print("--- Caught Exception : Print Info ---")
finally:
    print("Always Printed")



