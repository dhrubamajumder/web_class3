
menu = {
    'Pizza' : 40,
    'Pasta' : 50,
    'Burger' : 60,
    'Salad' : 70,
    'Coffee' : 80,
}

# Welcome Messege ------------------
print("Welcome to Python Resturant")

print("Pizza: 40\nPasta: 50\nBurger: 60\nSalad: 70\nCoffee: 80")
#/Welcome Messege -----------------

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
    

else:
    print(f"Order item{item_1} is not avaialable yet!")

another_order = input("Do you want to add another item? (Yes/No): ")


if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
        

    else:
        print(f"Orderd item {item_2} is not avaialable!")

print(f"The total amount of items to pay is :{order_total}")



