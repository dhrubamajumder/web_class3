# ------------------------------
# li = [1, 2, 3]
# print(dir(li))
# ------------------------------


# ------------------------------

class Car:
    color = "White"
    make = "Toyota"
    model = "Corolla"

    def __init__(self):
        print("I am called")
        
car1 = Car()
car2 = Car()
car3 = Car()

car1.color = "Red"
print(car1.color, car1.make, car1.model)




