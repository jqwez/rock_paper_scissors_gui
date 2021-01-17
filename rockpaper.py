import random

player_throw = ""
score = [0, 0, 0]

print("Welcome to Rock, Paper, Scissors!\n")
play_game = ""

while play_game != "play":
    play_game = input("Would you like to play? (enter Play or Help) :  ").lower()
    if play_game == "help":
        print("\n \nOnce you start the game, you can choose\n"
              "rock, paper, or scissors. I will,\n"
              "also choose one of those at random!\n"
              "I will go ahead and keep track of our games\n"
              "and tell you who is the winner if you type,\n"
              "'score' instead of rock,paper, or scissors!\n "
              "If you are done playing, then just type in quit\n"
              "to leave the game. Have fun!\n \n")
    if not "play":
        print("Please enter 'Play' or 'Help'")
        continue

print("Reaaaaaady???????")
while player_throw != "quit":
    player_throw = input("Rock, Paper, Scicsors, SHOOT! : ").lower()
    comp_throw = random.choice(["rock", "paper", "scissors"])

    if player_throw == comp_throw:
        print(f"My {comp_throw} vs. your {player_throw.capitalize()}. We tie!")
        score[2] += 1

    elif player_throw == "rock":
        if comp_throw == "scissors":
            print(f"My {comp_throw} vs. your {player_throw.capitalize()}. You win!")
            score[1] += 1
        elif comp_throw == "paper":
            print(f"My {comp_throw} vs. your {player_throw.capitalize()}. You lose!")
            score[0] += 1

    elif player_throw == "paper":
        if comp_throw == "rock":
            print(f"My {comp_throw} vs. your {player_throw.capitalize()}. You win!")
            score[1] += 1
        elif comp_throw == "scissors":
            print(f"My {comp_throw} vs. your {player_throw.capitalize()}. You lose!")
            score[0] += 1

    elif player_throw == "scissors":
        if comp_throw == "paper":
            print(f"My {comp_throw} vs. your {player_throw.capitalize()}. You win!")
            score[1] += 1
        elif comp_throw == "rock":
            print(f"My {comp_throw} vs. your {player_throw.capitalize()}. You lose!")
            score[0] += 1

    elif player_throw == "score":
        print(f"I have won {score[0]}, you have won {score[1]}, and we have tied {score[2]}!")

    elif player_throw == "help":
        print("Once you start the game, you can choose\n"
          "rock, paper, or scissors. I will,\n"
          "also choose one of those at random!\n"
          "I will go ahead and keep track of our games\n"
          "and tell you who is the winner if you type,\n"
          "'score' instead of rock,paper, or scissors!\n "
          "If you are done playing, then just type in quit\n"
          "to leave the game. Have fun!\n \n")

    else:
        if player_throw == "quit":
            print("Thanks for playing!!!! \n"
                  "\n"
                  f"Final Score: \n I won {score[0]}, you won {score[1]}, and we tied {score[2]}! ")
        else:
            print("What? Come on, ROCK, PAPER, or SCISSORS!")