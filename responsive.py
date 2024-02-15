first_name = input("whats your first name:")
last_name = input("whats your last name:")
full_name = first_name + " " + last_name
print(f"so your full name is {full_name}")

num = input("choose an number:")
num2 = input("choose an number:")
solution = int(num) + int(num2)
print(f"so if you add {num} and {num2} you'll get {solution}")

response = input("which spongebob character is your favorite spongebob, patrick, squidward, or sandy: ")

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
