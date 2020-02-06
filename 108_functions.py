# Functions

# Functions do one small task --> this makes them testable
# Can take inputs, perform task, and give an output
# It makes you're code more readable, maintainable and testable
# DRY code - don't repeat yourself
# Can run a block of code when called
# --> don't print inside function --> should return

# Syntax
# def function_name (arg1, arg2):
    # block of code
    # return

def say_hello():
    return 'hello'  #--> function with no arguments

def full_name(first, last):
    return first + ' ' + last # --> basic function with two arguments

# can call multiple functions within another function
# use casting/formatting in functions to avoid repeating in future code
# when calling functions on a different file, they must be imported first
# from ___ import * ---> to import all, can replace * with individual functions
# if we call a function on the importor page...
# will cause that to run on the importee file