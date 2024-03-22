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

print("Hello my name is {}".format(name2))
print("Hello my name is {:10}. Nice to meet you".format(name2))
print("Hello my name is {:<10}. Nice to meet you".format(name2))
print("Hello my name is {:>10}. Nice to meet you".format(name2))
