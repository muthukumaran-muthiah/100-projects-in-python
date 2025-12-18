import random

people = ["Mukun", "Yogi", "Raj", "Sri", "Ram"]

print(people[random.randint(0, len(people)-1)])

print(random.choice(people))