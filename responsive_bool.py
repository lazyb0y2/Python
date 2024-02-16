first_name = input("whats your first name:")
last_name = input("whats your last name:")
full_name = first_name + " " + last_name
print(f"so your full name is {full_name}")
# ----------------------------------------------------------------------------------------------------------------------

num = input("choose an number:")
num2 = input("choose another number:")
solution = int(num) + int(num2)
print(f"so if you add {num} and {num2} you'll get {solution}")
# ----------------------------------------------------------------------------------------------------------------------
# giving the user a response to there favorite character from spongebob
response = input(
    "which spongebob character is your favorite spongebob, patrick, squidward, krabs, plankton, or sandy: ")

if response == "spongebob":
    result = "your based"
elif response == "patrick":
    result = "you like dumb people"
elif response == "squidward":
    result = "your an adult"
elif response == "sandy":
    result = "your a simp"
elif response == "krabs":
    result = "your greedy and stingy"
elif response == "mr.krabs":
    result = "your greedy and stingy"
elif response == "plankton":
    result = "you don't exist"
elif response == "gary":
    result = "you are a god"
else:
    result = "okay keep your secrets"
print(result)
# ----------------------------------------------------------------------------------------------------------------------
# asking user how old they are and giving them a statement about there age
age = int(input("How old are you currently?: "))

if age >= 100:
    print("How? whats your secret")
elif age == 100:
    print("Sorry for being so blunt but your old!")
elif age >= 75:
    print("So your a senior")
elif age >= 50:
    print("So your middle aged")
elif age >= 18:
    print("So your an adult")
elif age >= 13:
    print("So your a teenager")
else:
    print("Your a child")
# ----------------------------------------------------------------------------------------------------------------------
# Logical operated (and,or,not) = used to check if two or more conditional statements is True
temp = int(input("Whats the temperature outside?: "))
# and means that both statements need be correct to be true
if (temp >= 0 and temp <= 30):
    print("The temperature is good today!")
    print("go outside!")
# or means one or both statements need to be correct for it to be true
elif (temp < 0 or temp > 30):
    print("The temperature is bad today!")
    print("Stay inside!")

# not means that if statements wrong It's correct
if not (temp >= 0 and temp <= 30):
    print("The temperature is bad today!")
    print("Stay inside!")

elif not (temp < 0 or temp > 30):
    print("The temperature is good today!")
    print("go outside!")
# ----------------------------------------------------------------------------------------------------------------------
