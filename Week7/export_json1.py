#/usr/bin/env python
import json
my_list = list(range(9))
my_list.append("ONE")
my_list.append("TWO")
print(my_list)

my_dict ={
    'key1' : 'value1',
    'key2' : 'value2',
}
my_dict['key3'] = my_list
my_dict['key4'] = ['1.1.1.1','2.2.2.2']
my_dict['key5'] = 'value5'
print(my_dict)
print(json.dumps(my_dict, indent=4))

with open("json_output1.json", mode="w") as f:
    json.dump(my_dict,f, indent=4)
print("Check json_output1.json")





