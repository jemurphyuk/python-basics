# For loops and iterators

# Syntax
# for i in <iterable>:
    # block of code with indented lines

cars = ['Skoda Felecia Fun', 'Mustang Boss 429', 'Vauxhall Corsa 1.2 SXi Twinspark', 'Aston Martin Vanquish', 'Jaguar 420G']

# for i in cars:
#     print(i.upper())

## Iterating over a dictionary
student1 = {
    'name': 'Arya Stark',
    'stream': 'Chemistry',
    'grade': '2.1',}

# for key in dictionary:
    # print(i)             --> this will give the keys

# for value in dictionary:
    # print(dictionary[i])

# # for i in student1:
# #     print(student1[i])  --> this will give individual values

# key and items together in a loop, print(key, dict[key])
#for i in student1:
    #print(f'{i.capitalize()}: {student1[i]}')

# Nested Loop iterations
# Looping over embedded lists
normal_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for list in nested_list:
#     # print(list)    --> optional line to show values of iterated list
#     for num in list:
#         print(num)   # this will give 1-9 values, line by line

# Iterating over a dictionary of dictionaries
dict_data = {1: {'name': 'stanley', 'money (£)': 5},
             2: {'name': 'geoff', 'money (£)': 15},
             3: {'name': 'ian', 'money (£)': 7}}

# To get output of
# - names
# - money

# for i in dict_data:
#     # print(dict_data[i]) --> optional line to show values of first dict, for keys 1, 2, 3
#     sub_dict = dict_data[i]
#     for item in sub_dict:
#         if type(sub_dict[item]) == int:
#             real_money = sub_dict[item] * 400000
#         else:
#             real_money = sub_dict[item]
#         print(f'{item.capitalize()}: {real_money}')


# While loops

# Syntax
# while condition:
#   block of code
#   something to alter condition

counter = 0  # --> initiating a counter

while counter <= 10:
    print(counter)
    print('increase counter')
    counter += 1            # ---> will keep repeating until counter reaches 10

# Other pattern for while loop
# while True:
    # block of code
    # control flow
    # if condition:
        # break ---> way of exiting the loop based on condition inside the loop




