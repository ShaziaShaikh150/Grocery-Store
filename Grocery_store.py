#Author: Shazia Shaikh
# Grocery Store

print("\t GROCERY STORE")
print("welcome to Ravals grocery store")
print("1.vegetables \n2.fruits \n3.bill")
a = {"vegetables": ["1 : carrot", "2 : peas"], "fruits": ["1 : apple", "2 : mango"]}
budget = int(input("enter your budget:"))
cost = 0


def options():
    global budget, cost
    print("do you want 1)vegetables 2)fruit 3)bill, Please type 1 for vegetables, 2 for Fruits and 3 for your final Bill")
    choice = int(input())

    if choice==1:
        b = a["vegetables"]
        print(b)
        print("Please type 1 for carrot and 2 for peas")
        choice1 = int(input("enter your choice1:"))

        if choice1 == 1:
            print(a["vegetables"][0])
            print("Price of carrot is 20rs per kg")
            x = int(input("enter your quantity:"))
            price = x * 20
            budget = budget - price

            if budget <= 0:
                print(f"you don't have that much money to buy ...you need more {abs(budget)}Rs to buy this")
            else:
                cost = cost + price
                print("rupees left is", budget)

            return options()
        elif choice1 == 2:
            print(a["vegetables"][1])
            print("Price of peas is 30rs per kg")
            y = int(input("enter your quantity:"))
            price = y * 30
            budget = budget - price

            if budget <= 0:
                print(f"you don't have that much money to buy ...you need more {abs(budget)}Rs to buy this")
            else:
                cost = cost + price
                print("rupees left is", budget)
            return options()
        else:
            print("Sorry, we have no such item")
            return options()

    elif choice == 2:
        print(a["fruits"])
        print("Please type 1 for Apple and 2 for Mango")
        choice1 = int(input("enter your choice1:"))
        if choice1 == 1:
            print(a["fruits"][0])
            print("Price of apple is 30rs per kg")
            x = int(input("enter your quantity:"))
            price = x * 30
            budget = budget - price

            if budget <= 0:
                print(f"you don't have that much money to buy ...you need more {abs(budget)}Rs to buy this")
            else:
                cost = cost + price
                print("rupees left is", budget)

            return options()
        elif choice1 == 2:
            print(a["fruits"][1])
            print("Price of mango is 40rs per kg")

            y = int(input("enter your quantity:"))
            price = y * 40
            if budget <= 0:
                budget = budget - price

                print(f"you don't have that much money to buy ...you need more {abs(budget)}Rs to buy this")
            else:
                cost = cost + price
                print("rupees left is", budget)
            return options()
        else:
            print("Sorry,we have no such item")
            return options()
    elif choice == 3:
        print(f"total bill is Rs {cost}")
    else:
        print("invalid")
        return options()


options()