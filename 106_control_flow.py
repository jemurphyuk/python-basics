# Control Flow
# if statements, else, elif (else if)
# Where code will execute, assertion dependent
    # Assertion is something that returns True or False

# # SYNTAX
# if condition:
    # block of code
# elif condition:
    # block2 of code
# else:
    # block3 of code

weather = 'rainy'
if weather == 'rainy':
    print('Take umbrella')
elif weather == 'stormy':
    print('Take a coat')
else:
    print('Take sunglasses')

print("I'm always running!!")

# Can use IN and AND to find multiples conditions in a variable, more flexibility
# weather = 'stormy and rainy'
if ('rainy' in weather) and ('stormy' in weather):
    print('stay at home')

# Must prioritse the more specific conditions at the top

age = 18
driver_license = False

if age >= 18 and driver_license == True:
    print('You can vote and drive')
elif age >= 18 and driver_license == False:
    print("You can only vote, you'll have to pass your test to drive")
elif 17 <= age < 18 and driver_license == True:
    print("You can drive, but you'll have to wait to vote")
elif 16 <= age < 18:
    print("Can't drive, can't vote, only getting a drink with a meal")
else:
    print("You should be in school, not thinking about drinking voting and driving!")
