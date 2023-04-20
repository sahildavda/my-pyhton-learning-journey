Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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
...     _______
... ---'   ____)____
...           ______)
...           _______)
...          _______)
... ---.__________)
... '''
... 
... scissors = '''
...     _______
... ---'   ____)____
...           ______)
...        __________)
...       (____)
... ---.__(___)
... '''
... 
... gameimages = [rock, paper, scissors]
... print("Welcome to my project on Rock Paper Scissors Game. Let's Play!!!\n")
... userchoice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper, 2 for Scissors..\n"))
... if userchoice >= 3 or userchoice < 0:
...   print("You chose an invalid number, Try Again!")
... else:
...   print(gameimages[userchoice])
...   compchoice = random.randint(0,2)
...   print("Computer Chose: ")
...   print(gameimages[compchoice])
...   if compchoice == 2 and userchoice == 0:
...     print("You Win!")
...   elif compchoice == 0 and userchoice == 2: 
...     print("You Lose!")
...   elif compchoice > userchoice:
...     print("You Lose!")
...   elif userchoice > compchoice:
...     print("You Win!")
...   elif compchoice == userchoice:
...     print("oops!! It's a Draw!!")
... 
