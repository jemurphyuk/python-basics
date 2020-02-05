import random

guess = input("Hey there, can you guess what single digit positive integer I'm thinking of? :    ")

if random.randint(1, 9) == int(guess):
    answer = "You got it right?!?! You must be a witch or wizard, I'll contact Hogwarts right away!"
else :
    answer = "Oh no never mind, guess you're not the bright spark we all thought you were!! :P"
print (answer)
