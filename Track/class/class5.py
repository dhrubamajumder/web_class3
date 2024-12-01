# ------------------------------------------
# class Variable, Instance Variable
# ------------------------------------------

import time
class Car:
    color = "White"
    pmanufacturer = "Toyota"
    brand = "Corolla"

    def __init__(self, a, b, c, d= 2024):
        self.make = a
        self.model = b
        self.color = c
        self.year = d

    def __str__(self):
        return f'{self.make}-{self.model}-{self.year}'
    
    def start_engine(self, t= 1):
        print("Strarting engine.......")
        time.sleep(t)
        print("Engine Startd ! Ready to Go !!!")


car1 = Car("Subaru", "Forester", "Bronze")
car1.color = "Blue"
car2 = Car("Toyota", "Prado", "White")
car3 = Car("Toyota", "Corolla","Red")

print(car1.color, car1.make, car1.model, car1.year)
print(car2.color, car2.make, car2.model, car2.year)
print(car3)

car1.start_engine(2)
car2.start_engine(5)
car3.start_engine(3)

# /////////////////////////////////////////////

# Inheritance 
# -------------------------------------

# class A:
#     def __init__(self):
#         print("Creating object for class A")

#     def jump(self):
#         print("yay! I am jumping   ")

# class AA(A):
#     def __init__(self):
#         print("Creating onject for class AA")

#     def jump(self):
#         print("yay! I am jumping !!!  ")
    
# a = A()
# b = A()
# c = AA()

# a.jump()
# c.jump()