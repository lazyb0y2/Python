# this is going to be for unruly code
# ----------------------------------------------------------------------------------------------------------------------
#   Keyword argument = argument preceded by an identifier when we pass them to a function
#                      The order of the argument doesn't matter, unlike positional arguments
#                      Python knows the names of the arguments that our function receives

def hello(first, middle, last):
    print("Hello ", +first+" "+middle+" "+last)


hello("Code", "The", "Bro")

# ----------------------------------------------------------------------------------------------------------------------
# **kwargs =    parameter that will pack all arguments into the dictionary
#               useful so that a function can accept a varying number of keywords' arguments

def hello(first, last):
    print("Hello ", + first + " ", +last)


hello(first="theo", last="bakes")