def print_name(name):
    print(f"Your name is {name}")

def print_age(age):
    '''
    Print Age passed to the print_age() function
    '''
    print(f"Your age is {age}")

print_name.__doc__ = "Print name passed to the print_name() function"
print(help(print_name))
print(help(print_age))

# For more detail info : https://realpython.com/documenting-python-code/


