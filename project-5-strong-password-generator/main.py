import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("Welcome to the strong password generator")
nr_letters = int(input("How many letters would you like to generate? "))
nr_numbers = int(input("How many numbers would you like to generate? "))
nr_symbols = int(input("How many symbols would you like to generate? "))

# Easy level
password = ""
for num in range(0,nr_letters):
    password += random.choice(letters)
for num in range(0,nr_numbers):
    password += random.choice(numbers)
for num in range(0,nr_symbols):
    password += random.choice(symbols)
print(f"Your generated password at the easy level is: {password}")

# Hard level
password_list = []
for num in range(0,nr_letters):
    password_list.append(random.choice(letters))
for num in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
for num in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
print(f"Your generated password at the hard level is: {''.join(password_list)}")
