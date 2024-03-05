# outputs words on a screen

# print("hello")
# ----------------------------------------------------------------------------------------------------------------------
# this is a variable it contains the value of the thing inside it
name = "bro"
# don't add " to a variable because it will become a string the outputs the variable name not what's contained
# print("name")
# print(name)
# this shows the variables value
# print(type(name))
# ----------------------------------------------------------------------------------------------------------------------
# you must add _ to two segmented words instead of a space, or it won't work
first_name = "Mark"
# print(first_name)
# you can combine multiple variable together
last_name = "damson"  # this could also work  # last_name = " damson"
full_name = first_name + last_name
full_name = first_name + " " + last_name
# print(full_name)
# ----------------------------------------------------------------------------------------------------------------------
# this is a comment --> #comments can't be seen when the code is running
# ----------------------------------------------------------------------------------------------------------------------
# when making a variable the either an int or float you don't use quotations/this "" because it will turn it into a string
age = 25
# print(age)
# after modifying the variable age, the print below shows the new one while the other shows the old one
age = age - 5
# print(age)
# its value is int instead of string now
# print(type(age))
age = age + .5
# print(age)
# its value is now float instead of string or int now
# print(type(age))
# ints are numbers without decimals while floats are numbers with decimals
# ----------------------------------------------------------------------------------------------------------------------
# print("your name is"full_name)[this won't work because somthing is missing]
# this one way for a variable to be added to a string statement
# print("your name is" + str(full_name))
# this is another way to add a variable into a string statement and the only way I know how add multiple to one as well
# print(f"your name is {full_name}")
# print(f"your name is {full_name} and your {age} years old")
# ----------------------------------------------------------------------------------------------------------------------
# multiple assignment = allows us to assign multiple variable at the same time in one line of code
name = "Bro"
age = 20
girlfriend = False
time = 8.22
name, age, girlfriend, time = "Bro", 20, False, 8.22
# print(name)
# print(age)
# print(girlfriend)
# print(time)
# ----------------------------------------------------------------------------------------------------------------------
# len shows how many lengths of the print
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

# print(x)
# print(type(x))
# print(y)
# print(type(y))
# print(z)
# print(type(z))
# ----------------------------------------------------------------------------------------------------------------------
pi = 3.14
ei = 2.53
oi = 1
# this rounds the number up or down
# print(round(pi))
# this will round it up no matter the number
# print(math.ceil(pi))
# this will round it down no matter the number
# print(math.floor(pi))
# abs/absolute value even if negative the number will be positive because it's absolute will be its positive form
# print(abs(pi))
# This time it by the power of any number you put
# print(pow(pi,2))
# this finds the square root of the number in round brackets
# print(math.sqrt(3))
# this prints out the biggest number
# print(max(oi, pi, ei))
# this prints out the smallest number
# print(min(oi, pi, ei))
# ----------------------------------------------------------------------------------------------------------------------
# list = used to store multiple items in a singular variable
# naruto is 0, bleach is 1, one piece is 2, dragon ball is 3, and jujutsu kaisen is 4
anime = ["Naruto", "Bleach", "One piece", "Dragon ball", "Jujutsu kaisen"]
# chooses which item on the list would be chosen just put a number in the []
anime[0] = "Food wars"  # instead of putting Naruto if I input anime[0] it will output Food wars
print(anime[0])
