import random
compans = ""
rand = random.randrange(1, 4)  
if rand == 1:
    compans == "Rock"
elif rand == 2:
    compans = "Paper"
else:
    compans = "Scissors"

inp = input("What do you choose? \n")
ans = inp.lower()

if ans == "rock" and compans == "Rock":
    print("Both chose Rock. It's a draw")
elif ans == "rock" and compans == "Paper":
    print("Paper beats Rock. You lose")
elif ans == "rock" and compans == "Scissors":
    print("Rock beats Scissors. You win")
elif ans == "paper" and compans == "Rock":
    print("Paper beats Rock. You win")
elif ans == "paper" and compans == "Paper":
    print("Both chose paper. It's a draw")
elif ans == "paper" and compans == "Scissors":
    print("Scissors beats paper. You lose")
elif ans == "scissors" and compans == "Rock":
    print("Rock beats scissors. You lose")
elif ans == "scissors" and compans == "Paper":
    print("Scissors beats paper. You win")
elif ans == "scissors" and compans == "Scissors":
    print("Both chose Scissors. It's a draw")
elif ans != "rock" or ans != "paper" or ans != "scissors":
    print("You need to choose Rock, Paper or Scissors as an answer")
