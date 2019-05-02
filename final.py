# Import JSON, make menu a JSON file, read file, ask for pizza_type, compare input with JSON, Free real estate!

from wit import Wit

import sys

import json

token = "WTILMQKSEMGNPMDFNI244VKTASMAWIC3"

client = Wit(token)

pizza_order = True # Ask for input, do you want to order or price check; change this variable based on the input

menu = json.loads(open('menu.json').read())

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

print question

print ""

slice_one = question[1]

if slice_one == "salami":

    pizza_type = slice_one

else:

    print "Pizza type cannot be determined? Did you spell it correctly and is it on the current menu?"

    sys.exit(0)

if pizza_type:

    print pizza_type

else:

    print "No pizza type given!"

    sys.exit(0)

print ""

print menu
