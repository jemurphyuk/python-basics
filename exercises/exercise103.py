str_age = input('What is your age?    ').strip()
age = int(str_age)
d_license = input("You possess a drivers license. True or False?    ").strip().capitalize()
driver_license = eval(d_license)

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
