import random

choices = ["rock", "paper", "scissors"]

computer = random.choices(choices)

player = input("rock, paper, or scissors?: ")

print(computer)
print(player)
