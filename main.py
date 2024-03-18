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
anime = ["Naruto", "Bleach", "One piece", "Dragon ball", "Jujutsu kaisen"]  # print(favorite[0]) is this
games = ["Sonic", "Zelda", "Call of duty", "Kingdom heart", "Hsr"]  # print(favorite[1]) is this
food = ["Spaghetti", "Rice and beans", "Chicken", "pizza", "Corn"]  # print(favorite[2]) is this
# 2D lists = a list of lists
favorite = [games, food, anime]  # I put the name of the variables, so they can be in one list
# chooses which item on a list would be chosen by an input of a number in the []
# anime[0] = "Food wars"  # instead of putting Naruto being number 0 on the list; this takes its place
# print(anime[0])
# prints out all of them by order of 0-4

# anime.append("Chainsaw man")
# anime.remove("Jujutsu kaisen")
# anime.pop()
# anime.insert(0, "Boruto") # adds another thing to the list and chooses where its placed
# anime.sort()
# anime.clear()

# for x in anime:
#    print(x)

# print(favorite) # if you add a [] it would choose what list while a second one will choose which word
# ----------------------------------------------------------------------------------------------------------------------
# tuple =   collection which is ordered and unchangeable
#           used to group together related data

student = ("bro", 21, "male",)

# print(student.count("bro")) # shows how many times this word, phrase, or number is used in the tuple
# print(student.index("bro")) # shows there position in the tuple

# for x in student:
# print(x)

# if "bro" in student:
# print("bro is here!") # if bro is inside the tuple, then it will print out bro
# ----------------------------------------------------------------------------------------------------------------------
# set = collection which is unordered, unidexed.no duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin") # added napkins to the set
# utensils.remove("fork") # removes fork from the set
# utensils.clear() # gets rid of the whole set
# dishes.update(utensils) # adds another set to the set
# dinner_table = utensils.union(dishes)

# print(dishes.difference(utensils)) # shows the difference between the two-set
# print(utensils.intersection(dishes)) # Shows the similarities between the two sets

# for x in dinner_table:
# print(x)
# ----------------------------------------------------------------------------------------------------------------------
# dictionary =  A changeable, unordered collection of a unique key:value pairs
#               Fast because they use hashing, allow us to access a value quickly
#             key   value
capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

capitals.update({'Germany': 'Berlin'}) # adds something new
capitals.update({'USA': 'Las Vegas'})
capitals.pop('China') # gets rid of item
capitals.clear() # clears everything

#print(capitals['Russia']) # if the key is to be input into the [] you will get the value
#print(capitals.get('China')) # when a key that exists or not is inputted, it will output its value
#print(capitals.keys()) # Shows the name of the keys instead of the value
#print(capitals.values())  # Does the opposite of .keys which is above
#print(capitals.items()) # Shows every item in the set

#for key, value in capitals.items():
#    print(key, value) # Shows the every key with there value besides them
# ----------------------------------------------------------------------------------------------------------------------
#   index operator  [] = gives access to a sequence's element (str,list,tuples)

title = "dude Rule"

if title[0].islower(): # video added () around title[0].islower
    title = title.capitalize() # Makes the variable use proper capitalization

first_section = title[0:4].upper() # out puts only value 0 to 4 while also upper casing it

print(first_section)
