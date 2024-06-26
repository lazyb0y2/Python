# slicing = creates a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

#name = "Bro Code"
# I'm going to be indexing in this section
#first_name = name[0:3]  # or [:3]
#last_name = name[4:8]  # or [4:]
#funky_name = name[0:8:2]  # or [::2]
#reversed_name = name[::-1]
#print(first_name)
#print(last_name)
#print(funky_name)
#print(reversed_name)
# ----------------------------------------------------------------------------------------------------------------------
# In this section im going to be slicing

#website1 = "https://google.com"
#website2 = "https://wikipedia.com"

# noinspection PyArgumentList
#slice = slice(8, -4)

#print(website1[slice])
#print(website2[slice])
# ----------------------------------------------------------------------------------------------------------------------
#   function = a block of code which is executed only when it is called

# I guess it allows you to use a trigger frase that activates its function if I input the name after def
# def hello(start_name, end_name, life):
#    print("hello!"+start_name+" "+end_name)
#    print("You are "+str(life)+" years old") # it doesn't like ints and floats
#    print("have a nice day!")


# hello("Bro", "Code", 21)
# ----------------------------------------------------------------------------------------------------------------------
#   return statement = Functions send python values/objects back to the caller.
#                      These values/objects are known as the function's return value

#def multiply(number1, number2):
#    result = number1 * number2
#    return number1 * number2

#x = multiply(6, 8)

#print(x)
# ----------------------------------------------------------------------------------------------------------------------
# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped version of a variable can be created

#name = "Bro" # global scope (available inside & outside functions)

#def display_name():
#    name = "Code"   # local scope (available only inside this function)
#    print(name)

#display_name()
#print(name)
# L = Local
# E = Enclosing
# G = Global
# B = Built-in
# ----------------------------------------------------------------------------------------------------------------------
# *args =   parameter that will pack all arguments into a tuple
#           useful so that a function can accept a varying number of arguments
#     (num1 + num2)
#def add(*stuff):
#    sum = 0
#    stuff = list(stuff)
#    stuff[0] = 0 # stops it from adding
#    for i in stuff:
#        sum += i
    #sum = num1 + num2
#    return sum


#print(add(20, 50, 46))
# ----------------------------------------------------------------------------------------------------------------------
# str.format() =    optional method that gives users
#                   more control when displaying output

animal = "cow"
item = "moon"

#print("The "+animal+" jumped over the "+item)
#print("The {} jumped over the {}".format(animal, item))
#print("The {1} jumped over the {0}".format(animal, item)) # positional argument
#print("The {animal} jumped over the {item}".format(animal="cow", item="moon")) # keyword argument

#text = "The {} jump over the {}"
#print(text.format(animal, item))

name2 = "dude"

#print("Hello my name is {}".format(name2))
#print("Hello my name is {:10}. Nice to meet you".format(name2))
#print("Hello my name is {:<10}. Nice to meet you".format(name2)) # does what the one on top does
#print("Hello my name is {:>10}. Nice to meet you".format(name2)) # does the opposite of the two above
#print("Hello my name is {:^10}. Nice to meet you".format(name2)) # does the same thing as line 99 and 100

number = 1000

#print("The number pi is {:.3f}".format(number)) # the number in the {} dictates how much is shown at the end of the .
#print("The number pi is {:,}".format(number)) # adds a , after every hundreds place
#print("The number pi is {:b}".format(number)) # shows a binary representation of the number
#print("The number pi is {:o}".format(number)) # shows as an octal number
#print("The number pi is {:x}".format(number)) # shows as a hexadecimal lower case
#print("The number pi is {:X}".format(number)) # shows as a hexadecimal upper case
#print("The number pi is {:e}".format(number)) # shows as a scientific notation lower case
#print("The number pi is {:E}".format(number)) # shows as a scientific notation upper case
# ----------------------------------------------------------------------------------------------------------------------
import random

#x = random.randint(1, 6)
#y = random.random()

#myList = ['rock', 'paper', 'scissor']
#z = random.choice(myList)

#cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K"]
#random.shuffle(cards)

#print(x)
#print(y)
#print(z)
#print(cards)
# ----------------------------------------------------------------------------------------------------------------------
import os

#path = "/Users/319501/Downloads"

#if os.path.exists(path):
#    print("That location exists!")
#    if os.path.isfile(path):
#        print("That is a file")
#    elif os.path.isdir(path):
#        print("That's a directory")
#else:
#    print("That location doesn't exist!")
# ----------------------------------------------------------------------------------------------------------------------
# module = a file containing python code, May contain functions, classes, ect.
# Used with modular programming, which is to separate a program into parts

#import message
#import message as msg
#from messages import hello, bye
#from messages import *
#help("modules")

#messages.hello()
#messages.bye()
##msg.hello()
#msg.bye()
#hello()
#bye()
# ----------------------------------------------------------------------------------------------------------------------
#def message(what, number):
#    print("Enter", what, "number", number)

# invoke the function

#message("telephone", 11)
#message("price", 5)
#message("number", "number")
# ----------------------------------------------------------------------------------------------------------------------








