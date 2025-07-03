import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Rock wins against scissors
# Scissors win against paper
# Paper win against rock

print("Welcome to the Rock, Paper, and Scissors game!")
game = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if game == 0:
    print(rock)
elif game == 1:
    print(paper)
else:
    print(scissors)

hands = [rock, paper, scissors]
index = random.randint(0, 2)
final = hands[index]

print(f"Computer chose {final}")

if game == 0 and final == rock:
    print("Draw!")
elif game == 0 and final == paper:
    print("You lose!")
elif game == 0 and final == scissors:
    print("You win!")
elif game == 1 and final == rock:
    print("You win!")
elif game == 1 and final == paper:
    print("Draw!")
elif game == 1 and final == scissors:
    print("You lose!")
elif game == 2 and final == rock:
    print("You lose!")
elif game == 2 and final == paper:
    print("You win!")
elif game == 2 and final == scissors:
    print("Draw!")
else:
    print("Try again!")