import random
choice = input("What's your choice? Heads or Tails? ")
system_choice = random.randint(1,1000)

if system_choice%2 != 0 and choice == "Heads":
    print("You win!")
elif system_choice%2 == 0 and choice == "Tails":
    print("You win!")
else:
    print("You lose!")