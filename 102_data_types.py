# Strings, characters put together in a list
# defined by '' or ""

# Joining of two strings, just add, concatenation
first_name = 'James'
last_name = 'Murphy'
print (first_name + ' ' + last_name)
full_name = (first_name + ' ' + last_name)
print(full_name)

# Interpolation, inject a string into another string
welcome = "welcome to the danger zone"
print (f'{full_name} welcome')

# Special methods for strings
my_string = "   Hello, i'm amazing"
# .count(), for specific letter or characters
print (my_string.strip()) # remove white space before or after
# len function not method
print(len(my_string))
print (my_string.upper()) # all letters caps
print (my_string.strip().split(","))


