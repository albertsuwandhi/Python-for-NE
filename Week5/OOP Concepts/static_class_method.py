#/usr/bin/env python3

# Object : Attribute and Method
class Hero(object):
    __count = 0
    def __init__(self,inputName,inputAge, inputPower):
    # All are private variable/attributes
        self.__name = inputName
        self.__age = inputAge
        self.__power = inputPower
        Hero.__count += 1
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
    # static method (decorator) -- tied to class and object
    @staticmethod
    def getCount1():
        return Hero.__count

    # method tied to class only not object
    def getCount2():
        return Hero.__count

    # method tied to class only 
    @classmethod
    def getCount3(cls):
        return cls.__count

    # method tied to object only --> self
    def getCount4(self):
        return Hero.__count

Zelda = Hero("Zelda", 22, 100)
print(Zelda.getCount1())
print(Hero.getCount1())
Mario = Hero("Mario", 20, 90)
print(Mario.getCount3())
Luigi = Hero("Luigi", 18, 80)
print(Luigi.getCount4())
print(Hero.getCount2())







