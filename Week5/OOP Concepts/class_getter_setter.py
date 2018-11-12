#/usr/bin/env python3

# Object : Attribute and Method
class Hero(object):
    def __init__(self,inputName,inputAge, inputPower):
    # All are private variable/attributes
        self.__name = inputName
        self.__age = inputAge
        self.__power = inputPower
    # getter
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getPower(self):
        return self.__power
    # setter
    def changeName(self,x):
        self.__name = x
    def decrementPower(self,x):
        self.__power -= x

hero1 = Hero("Zelda", 22, 100)
print(hero1.__dict__)
# This won't work
#hero1.__power = 175
print(hero1.getName())
print(hero1.getAge())
print(hero1.__dict__)
hero1.changeName("Mario")
hero1.decrementPower(10)
print(hero1.__dict__)






