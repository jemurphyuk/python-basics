# Create a program to ask user fro following details
# name, height, colour, a secret number
# capture inputs
# print a tailored welcome message to user,
# print other details it gathered, except the secret of course
# hint: think about casting data type
print("Hello there, what is your name?")
name = input()
print ("Hello", name, "!!!!")
print ("How tall are you in centimetres?")
height = input()
print ("What's your favourite colour?")
colour = input()
print ("And a secret number??")
number = input()
print (f"So {name.capitalize()}, you're {height} centimetres tall, {colour.lower()} is your favourite, and your secret number is private!!")
