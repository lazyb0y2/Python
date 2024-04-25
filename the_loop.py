# while loop = a statement that will execute its block of code
#              as long as it's condition remains true
import time

#name = ""
#while len(name) == 0:
#   name = input("Enter your name: ")

#print("Hello" + " " + name)
# ----------------------------------------------------------------------------------------------------------------------
#name = None

#while not name:
#    name = input("Enter your name: ")

#    print("Hello " + name)
# ----------------------------------------------------------------------------------------------------------------------
# for loop =   a statement that will execute its block of code
#              a limited amount of times
#
#              while loop = unlimited
#              for loop = limited

#for i in range(10):
#print(i + 1)
#     c,u,n = count, up, number
#       starting ! end !c,u,n !
#for i in range(50, 100 + 1, 2):
#    print(i)

#for i in "Bro Code":
#    print(i)
#  starting number  >10<
#   ending number        >0<
#   makes it count down     >-1<
#for second in range(10, 0, -1):
#    print(second)
#     time.sleep(1)
#print("Happy New Year!")
# ----------------------------------------------------------------------------------------------------------------------
# nested loops =    The "inner loop" will finish all of its iterations before
#                   finishing one iteration of the "outer loop"

#rows = int(input("How many rows?: "))
#columns = int(input("How many columns?: "))
#symbol = input("Enter a symbol to use?: ")

#for i in range(rows):
#    for j in range(columns):
#        print(symbol, end="")
#    print()
# ----------------------------------------------------------------------------------------------------------------------
# Loop Control Statement = changes a loop's execution from its normal sequence

# break =      used to terminate the loop entirely
# continue =   skips to the next iteration of the loop.
# pass =       does nothing, acts as a placeholder

#while True:
#    name = input("Enter your name: ")
#    if name != "":
#        break

#phone_number = "123-456-7890"

#for i in phone_number:
#    if i == "-":
#        continue
#    print(i, end="")

#for i in range(1, 21):

#    if i == 13:
#        pass
#    else:
#        print(i)
# ----------------------------------------------------------------------------------------------------------------------
# this is the code from 3.2.1.3 lab

#secret_number = 777

#print(
#    """
#    +================================+
#    | Welcome to my game, muggle!    |
#    | Enter an integer number        |
#    | and guess what number I've     |
#    | picked for you.                |
#    | So, what is the secret number? |
#    +================================+
#    """)
#guess_number = input("What is the secret number: ")
#guess_number = int(guess_number)

#while guess_number != secret_number:

#    if guess_number != secret_number:
#        print("Ha ha! You're stuck in my loop!")

#print("Well done, muggle! You are free now.")
# ----------------------------------------------------------------------------------------------------------------------
#while True:
#    word = input("Enter a word: ")
#    if word.lower() == "chupacabra":
#        print("You've successfully left the loop.")
#        break
# ----------------------------------------------------------------------------------------------------------------------








