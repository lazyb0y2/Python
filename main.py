# outputs words on a screen
print("hello")
# ----------------------------------------------------------------------------------------------------------------------
# this is a variable it contains the value of the thing inside of it
name = "bro"
# don't add " to a variable because it will become a string the outputs the variable name not what's contained
print("name")
print(name)
# this shows the variables value
print(type(name))
# ----------------------------------------------------------------------------------------------------------------------
# you must add _ to two segmented words instead of a space, or it won't work
first_name = "Mark"
print(first_name)
# you can combine multiple variable together
last_name = "damson"  # this could also work  # last_name = " damson"
# full_name = first_name + last_name
full_name = first_name + " " + last_name
print(full_name)
# ----------------------------------------------------------------------------------------------------------------------
# this is a comment --> #comments can't be seen when the code is running
# ----------------------------------------------------------------------------------------------------------------------
# when making a variable the either an int or float you don't use quotations/this "" because it will turn it into a string
age = 25
print(age)
# after modifying the variable age  the print below shows the new one while the other shows the old one
age = age - 5
print(age)
# its value is int instead of string now
print(type(age))
age = age + .5
print(age)
# its value is now float instead of string or int now
print(type(age))
# ints are numbers without decimals while floats are numbers with decimals
# ----------------------------------------------------------------------------------------------------------------------
# print("your name is"full_name)[this won't work because somthing is missing]
# this one way for a variable to be added to a string statement
print("your name is" + str(full_name))
# this is another way to add a variable into a string statement and the only way I know how add multiple to one as well
print(f"your name is {full_name}")
print(f"your name is {full_name} and your {age} years old")
# ----------------------------------------------------------------------------------------------------------------------
# multiple assignment = allows us to assign multiple variable at the same time in one line of code
# name = "Bro"
# age = 20
# girlfriend = False
# time = 8.22
name, age, girlfriend, time = "Bro", 20, False, 8.22
print(name)
print(age)
print(girlfriend)
print(time)
# ----------------------------------------------------------------------------------------------------------------------
# len shows how many length of the print
title = "ultimate life form"
# print(len(title))
# this tells us what number this character was designate in order
# print(title.find("e"))
# this code automatically capitalizes the word for you
# print(title.capitalize())
# this put everything in all caps
# print(title.upper())
# this makes everything lower cased
# print(title.lower())
# this checks to see the print is an int
# print(title.isdigit())
# this checks to see if the variable has a space or not if it has a space it's False if not True
# print(title.isalpha())
# counts the amount of time this character was used
# print(title.count("i"))
# replaces a certain character with another character
# print(title.replace("t", "l"))
# multiples it how many times you want
# print(title*3)
# ----------------------------------------------------------------------------------------------------------------------
x = 1  # this is an int
y = 2.0  # this is a float
z = "3"  # this is a string
# adding float, str, or int can change the type of variable
x = float(x)
y = str(y)
z = int(z)

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))
# ----------------------------------------------------------------------------------------------------------------------
