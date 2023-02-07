import random

names = input("Enter the names separated by a comma.\n").split(",")

list = len(names)

pos = random.randint(0, list-1)

print(f"{names[pos]} will clear the bill for the day.")


