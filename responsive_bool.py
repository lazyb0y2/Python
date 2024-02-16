first_name = input("whats your first name:")
last_name = input("whats your last name:")
full_name = first_name + " " + last_name
print(f"so your full name is {full_name}")
# ----------------------------------------------------------------------------------------------------------------------

num = input("choose an number:")
num2 = input("choose an number:")
solution = int(num) + int(num2)
print(f"so if you add {num} and {num2} you'll get {solution}")
# ----------------------------------------------------------------------------------------------------------------------

response = input("which spongebob character is your favorite spongebob, patrick, squidward, krabs, plankton, or sandy: ")

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
user_age = input("How old are you currently: ")

if user_age >= 13:
    print("So your a teenager")
elif user_age >= 18:
    print("So your an adult")
elif user_age >= 50:
    print("So your middle aged")
elif user_age >= 75:
    print("So your a senior")
elif user_age == 100:
    print("Sorry for being so blunt but your old!")
elif user_age >= 100:
    print("How? whats your secret")
else:
    print("Your a child")
