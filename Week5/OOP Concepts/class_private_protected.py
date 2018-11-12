#/usr/bin/env python3

# Object : Attribute and Method
class Hero(object):
    #class variable
    count = 0
    def __init__(self,inputName,inputAge):
    # name and age are instance variable
        self.name = inputName
        self.age = inputAge
    # private, can only be accessed within the class
        self.__height = 170
    # protected, can be changed but pls not change it
        self._weight = 80
    # increment count every time __init is called
        Hero.count += 1
    def printName(self):
        print("Your Name is : ", self.name)
    def addAge(self,x):
        self.age += x
    def getAge(self):
        return self.age

hero1 = Hero("Zelda", 22)
print(hero1.__dict__)
# This will generate error
# print(hero1.__height)
# Assign value --> will create instance variable __height, 
# but it won't override/not the same as the private variable
hero1.__height = 175
print(hero1.__dict__)
#Result : {'_weight': 80, 'age': 22, '__height': 175, '_Hero__height': 170, 'name': 'Zelda'}
print(hero1.__height)
print("-"*60)
print(hero1.__dict__)
hero1._weight = 100
print(hero1.__dict__)
print(hero1._weight)





