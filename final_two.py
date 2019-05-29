from wit import Wit 

from pizzapi import * 

import sys 

import json 

token = "WTILMQKSEMGNPMDFNI244VKTASMAWIC3"

client = Wit(token)

# Add Wit input, take output, look for pizza_order, if found continue, otherwise exit

print ("###################################")

print (" _    _ _ _  ______ _              ")

print ("| |  | (_) | | ___ (_)             ")

print ("| |  | |_| |_| |_/ /_ __________ _ ")

print ("| |/\| | | __|  __/| |_  /_  / _` |")

print ("\  /\  / | |_| |   | |/ / / / (_| |")

print (" \/  \/|_|\__\_|   |_/___/___\__,_|")

print ("")

print ("WitPizza v1.0")

print ("")

print ("###################################")

print ("")

print ("Welcome to WitPizza!")

print ("")

print("Please enter your information.")

print("")

name_first = str(input("Please enter your first name: "))

name_last = str(input("Please enter your last name: "))

email = str(input("Please enter your email adress: "))

phone = str(input("Please enter your phone number: "))

customer = Customer(name_first, name_last, email, phone)

living_adress = str(input("Please enter your adress and number: "))

city = str(input("Please enter your city: "))

state = str(input("Please enter your state: "))

zip_code = str(input("Please enter your zip code: "))

adress = Address(living_adress, city, state, zip_code)

store = adress.closest_store()

order = Order(store, customer, adress)

card = PaymentObject('4100123422343234', '0115', '777', '90210')

menu = store.get_menu()

print("Search the menu: ")

print("")

menu_name = str(input("What would you like to search the menu for? "))

menu.search(Name=menu_name) 

menu_add = str(input("Would you like to add an item? "))

if menu_add == "Yes": 

    menu_add_item = str(input("Please enter the code of the item you would like to add: "))

    order.add_item(menu_add_item)

    menu_add_another = str(input("Would you like to add another item? "))

    while menu_add_another == "Yes": 

        menu_add_item = str(input("Please enter the code of the item you would like to add: "))

        order.add_item(menu_add_item)

        menu_add_another = str(input("Would you like to add another item? "))
    
    if menu_add_another == "No":

        menu_search_again = str(input("Would you like to search the menu again? "))

        if menu_search_again == "No": 

            order_decision = str(input("Would you like to order the selected items? "))

            if order_decision == "Yes": 

                order.pay_with(card)

                print("")

                print("Order successful!")

                print("")
            
            else: 

                print("Goodbye!")

                print("")

                sys.exit(0)

        while menu_search_again == "Yes": 

            menu_name = str(input("What would you like to search the menu for? "))

            menu.search(Name=menu_name)

            menu_add = str(input("Would you like to add an item? "))

            if menu_add == "Yes": 

                menu_add_item = str(input("Please enter the code of the item you would like to add: "))

                order.add_item(menu_add_item)

                menu_add_another = str(input("Would you like to add another item? "))

                while menu_add_another == "Yes": 

                    menu_add_item = str(input("Please enter the code of the item you would like to add: "))

                    order.add_item(menu_add_item)

                    menu_add_another = str(input("Would you like to add another item? "))
        
            else: 

                menu_search_again = str(input("Would you like to search the menu again? "))

                if menu_search_again == "No":

                    order_decision = str(input("Would you like to order the selected items? "))

                    if order_decision == "Yes": 

                        order.pay_with(card)

                        print("")

                        print("Order successful!")

                        print("")

                    else: 

                        print("Goodbye!")

                        print("")

                        sys.exit(0)
                
                while menu_search_again == "Yes":

                    menu_name = str(input("What would you like to search the menu for? "))

                    menu.search(Name=menu_name)

                    menu_add = str(input("Would you like to add an item? "))

                    if menu_add == "Yes": 

                        menu_add_item = str(input("Please enter the code of the item you would like to add: "))

                        order.add_item(menu_add_item)

                        menu_add_another = str(input("Would you like to add another item? "))

                        while menu_add_another == "Yes": 

                            menu_add_item = str(input("Please enter the code of the item you would like to add: "))

                            order.add_item(menu_add_item)

                            menu_add_another = str(input("Would you like to add another item? "))
        
                        else: 

                         menu_search_again = str(input("Would you like to search the menu again? "))

                
else: 

    menu_search_again = str(input("Would you like to search the menu again? "))

    if menu_search_again == "No":

                    order_decision = str(input("Would you like to order the selected items? "))

                    if order_decision == "Yes": 

                        order.pay_with(card)

                        print("")

                        print("Order successful!")

                        print("")

                    else: 

                        print("Goodbye!")

                        print("")

                        sys.exit(0)

    while menu_search_again == "Yes":

        menu_name = str(input("What would you like to search the menu for? "))

        menu.search(Name=menu_name)

        menu_add = str(input("Would you like to add an item? "))

        if menu_add == "Yes": 

            menu_add_item = str(input("Please enter the code of the item you would like to add: "))

            order.add_item(menu_add_item)

            menu_add_another = str(input("Would you like to add another item? "))

            while menu_add_another == "Yes": 

                menu_add_item = str(input("Please enter the code of the item you would like to add: "))

                order.add_item(menu_add_item)

                menu_add_another = str(input("Would you like to add another item? "))
        
        else: 

            menu_search_again = str(input("Would you like to search the menu again? "))

            if menu_search_again == "No":

                    order_decision = str(input("Would you like to order the selected items? "))

                    if order_decision == "Yes": 

                        order.pay_with(card)

                        print("")

                        print("Order successful!")

                        print("")

                    else: 

                        print("Goodbye!")

                        print("")

                        sys.exit(0)




        


        