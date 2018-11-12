#/usr/bin/env python3

# Object : Attribute and Method
class Hero(object):
    #class variable
    count = 0
    def __init__(self,inputName,inputAge):
    # name and age are instance variable
        self.name = inputName
        self.age = inputAge
    # increment count every time __init is called
        Hero.count += 1
    def printName(self):
        print("Your Name is : ", self.name)
    def addAge(self,x):
        self.age += x
    def getAge(self):
        return self.age

hero1 = Hero("Zelda", 22)
hero2 = Hero("Megaman", 15)
print("Hero.Count is : ", Hero.count)
print("hero1 is : ", hero1)
print("Attribute of hero1 : ", hero1.__dict__)
print("Attribute of hero1 : ", hero2.__dict__)
hero2.printName()
hero2.addAge(3)
print("Age of hero2 is", hero2.getAge()) 
