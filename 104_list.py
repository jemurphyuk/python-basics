# Lists

# defining a list
# syntax --> []
# we can dynamically define or redefine a list
crazy_landlords = ['Mr Richards', 'Raj', 'Mr Shrik', 'Zemu',]
print(crazy_landlords)
# access an item in list using indexes
# lists are organised using indexes
# to access first item 'Mr Richards', we need index no.0 and so on
print(crazy_landlords[0])
# We can also redefine at a specific index
    # Change Zemu to Zulu
crazy_landlords[3] = 'Zulu'
print(crazy_landlords)

# to select last record, use [-1]
        # an aside: list_length = len(list) to find end of list, last_index = list_length - 1
# add record to list
    # .append(object)
crazy_landlords.append('Lana')
print(crazy_landlords)

# add record at specific index
    # use .insert(x, y) where x is index and y is what to insert
crazy_landlords.insert(1, 'Bob')
print(crazy_landlords)

# Remove item from list by value, use .delete
# Remove item from list by index, use .pop
    # .pop() will remove last entry of index

# We can have a mixed data list of strings, ints, floats etc.
# Can also have nested list

# Tuples - immutable lists that can't be changed when created
    # notation:     tuple = ()
my_tuple = (2, 'hello', 22, 'value')
# can be indexed using tuple[x]
# resetting such as: tuple[0] = name :is not possible
# tuple[name][x] to access character of a string, for x = 0, 'n' would be printed

# Range slicing
# between x and y [x:y] where x is inclusive but y is not
# [a:b:c] where a is first, b is last not inclusive, c is gap
    # eg. for even/odd in set of continous integers, set to 2
    # POI - can leave blanks at each stage, will have defaults of [start_index:end_index:1]
    # can also count backwards from end using -ve value for c, where defaults [end_index:start_index:-1]
print(my_tuple[::-1])

# Dictionaries
# Need to know where 'crazy_landlords' live, we need more info
# Dictionaries are organised using key value pairs
# enable the reading of specific location
my_dictionary = {'key': 'value1', 'other_key': 'value2'} # key and value can be any string or int data type
landlord_dictionary = {'name': 'James', 'phone': '01234567789'}
print(landlord_dictionary)

# read one entry in dictionary (read the value of one key)
print(landlord_dictionary['phone'])
# Add a key value pair
landlord_dictionary['address'] = 'Silver End'
# Update the value in a key
landlord_dictionary['phone'] = '09876543221'
print(landlord_dictionary)
# destroy one key value pair using .pop again with key, will remove key and value
# Select all keys --> .keys()
# Select all values --> .values()
