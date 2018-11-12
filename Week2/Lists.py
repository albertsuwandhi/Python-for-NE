#!/usr/bin/env python3
list1 = [1, "Yes", 2, "No",1.5]
print("Type of list1 :", type(list1))
print("Content of list1 : ", list1)
'''
print("Content of list1 : ")
for i in range(len(list1)):
    print(list1[i])
'''
print("Append list1 with 8.8.8.8")
list1.append('8.8.8.8')
print("list1 after append : ", list1)
print("Extend list1 with 1.1.1.1 and 443")
list1.extend(['1.1.1.1',443])
print("list1 after extend : ", list1)
print("list1 + [1,2,3] = ", list1 + [1,2,3])
print("list1 :", list1)
del list1[-1]
print("list1 after del list1[-1] : ", list1)
print("POP Operation")
for idx in range(len(list1)):
    list1.pop(0)
    print("list1 : ", list1)
print("-"*80)
#put special attention to lists - MUTABLE
mylist = [1,2,3]
print("mylist       :", mylist)
print("ID mylist    :", id(mylist))
new_list = mylist
print("new_list     :", new_list)
print("ID new_list  :", id(new_list))
new_list.append('8.8.8.8')
print("Append new_list with 8.8.8.8")
print("new_list     :", new_list)
print("mylist       :", mylist)
print ("---- List Slicing ----")
list1 = [1, "Yes", 2, "No",1.5,'8.8.4.4','whatever']
print("list1         :", list1)
print("list1[0:4]    :",list1[0:4])
print("list1[:3]     :",list1[:3])
print("list1[1:4]    :",list1[1:4])
print("list1[2:]     :",list1[2:])
print("list1[-3:-1]  :",list1[-3:-1])
del list1[1]
print("list1         :", list1)
list1.insert(1,1)
print("list1         :", list1)
list1. remove('whatever')
print("list1         :", list1)
print("Count of 1 : ", list1.count(1))
print("Length of list1 : ", len(list1))







    


