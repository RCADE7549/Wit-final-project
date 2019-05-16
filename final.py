# Import JSON, make menu a JSON file, read file, ask for pizza_type, compare input with JSON, Free real estate!

from wit import Wit

import sys

import json

token = "WTILMQKSEMGNPMDFNI244VKTASMAWIC3"

client = Wit(token)

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

print ("Available Actions: ")

print ("")

print ("1: Place an order")

print ("2: Look at the menu")

print ("99: Exit")

print ("")

decision = int(input("What would you like to do? "))

if decision == 1:

    pizza_order = True

    print ("")

    print ("Available menus: ")

    print ("")

    print ("1: Pizza")

    print ("99: Exit")

    print ("")

    pizza_order_menu_decision = int(input("Which menu would you like to order from? "))

    print ("")

    if pizza_order_menu_decision == 1:

        menu = json.loads(open('menu_with_prices.json').read())

        count = -2

        with open("menu_with_prices.json") as f:

            for line in f:

                count += 1

            new_count = 0

            while new_count < count:

                slice = menu[new_count]

                print (slice)

                new_count += 1

    elif pizza_order_menu_decision == 99:

        print ("Goodbye!")

        print("")

        sys.exit(0)

    else:

        print ("The requested menu is not available!")

        print ("Please rerun the program and try again!")

        print("")

        sys.exit(0)


elif decision == 2:

    print ("")

    print ("Available menus: ")

    print ("")

    print ("1: Pizza")

    print ("99: Exit")

    print ("")

    pizza_menu_decision = int(input("Which menu would you like to look at? "))

    print ("")

    if pizza_menu_decision == 1:

        menu = json.loads(open('menu_with_prices.json').read())

        count = -2

        with open("menu_with_prices.json") as f:

            for line in f:

                count += 1

            new_count = 0

            while new_count < count:

                slice = menu[new_count]

                print (slice)

                new_count += 1

    elif pizza_menu_decision == 99:

        print ("Goodbye!")

        print("")

        sys.exit(0)

    else:

        print ("The requested menu is not available!")

        print ("Please rerun the program and try again!")

        print("")

        sys.exit(0)

elif decision == 99:

    print("")

    print("Goodbye!")

    print("")

    sys.exit(0)

else:

    print("")

    print("The requested action is not available!")

    print("Please rerun the program and try again!")

    print("")

    sys.exit(0)

def wit_response(message_text):

    resp = client.message(message_text)

    entity = None

    value = None

    try:

        entity = list(resp['entities'])[0]

        value = resp['entities'][entity][0]['value']

    except:

        pass

    return (entity, value)

pizza_type = None

question = (wit_response("Order me a salami pizza"))

print (question)

print ("")

slice_one = question[1]

if slice_one == "salami":

    pizza_type = slice_one


else:

    print ("Pizza type cannot be determined? Did you spell it correctly and is it on the current menu?")

    print("")

    sys.exit(0)

if pizza_type:

    print (pizza_type)


else:

    print ("No pizza type given!")

    print("")

    sys.exit(0)
