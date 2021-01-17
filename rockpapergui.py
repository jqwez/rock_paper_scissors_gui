from tkinter import *
from tkinter import ttk

game_running = False


root = Tk()
root.title("Rock, Paper, Scissors! by Jeremy Vasquez")
root.geometry("400x190")

mainframe = ttk.Frame(root, padding=" 3 3 3 3 ", borderwidth="5")
mainframe.grid(column=0, row=0, sticky="N W S E")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

playerframe = ttk.Frame(root, padding=" 3 3 3 3", borderwidth="5")
playerframe.grid(column=1, row=0, sticky="N W S E")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

computer_talk = StringVar(root, value="Welcome")
score_c = StringVar(root, value=0)
score_p = StringVar(root, value=0)
score_t = StringVar(root, value=0)
score = (f"I have won {score_c}, you have won {score_p}, and we have tied {score_t}!")

comp_talk = ttk.Label(mainframe, textvariable=computer_talk, wraplength="250").grid(column=0, row=0)

def start_game():
    computer_talk.set("Rock, Paper, Scissors, SHOOT! :")
    global score_c
    global score_p
    global score_t
    score_c = 0
    score_p = 0
    score_t = 0
    global game_running
    game_running = True
    global player_throw
    while game_running is True:
        player_throw = ""
        player_throw.wait_variable
        # comp_throw = random.choice(["rock", "paper", "scissors"])
        comp_throw = "rock"
        if player_throw == comp_throw:
            computer_talk.set(f"My {comp_throw} vs. your {player_throw.capitalize()}. We tie!")
            score[2] += 1
        else:
            break

def quit_game():
    computer_talk.set(f"Thanks for playing!!!! \n"
                  "\n"
                  "Final Score: \n I won {score[0]}, you won {score[1]}, and we tied {score[2]}! ")
    game_running = False

def player_rock():
    computer_talk.set("rock")
    player_throw = "rock"

def player_paper():
    computer_talk.set("paper")
    player_throw = "rock"

def player_scissors():
    computer_talk.set("scissors")
    player_throw = "rock"

def ask_score():
    computer_talk.set(score)

def help():
    computer_talk.set("Once you start the game, you can choose\n"
              "rock, paper, or scissors. I will,\n"
              "also choose one of those at random!\n"
              "I will go ahead and keep track of our games\n"
              "and tell you who is the winner if you type,\n"
              "'score' instead of rock,paper, or scissors!\n "
              "If you are done playing, then just type in quit\n"
              "to leave the game. Have fun!")

#Player Throws

ttk.Button(playerframe, text="Start", command=start_game).grid(column=1, row=0)
ttk.Button(playerframe, text="Quit", command=quit_game).grid(column=1, row=1)
ttk.Button(playerframe, text="Rock", command=player_rock).grid(column=1, row=2)
ttk.Button(playerframe, text="Paper", command=player_paper).grid(column=1, row=3)
ttk.Button(playerframe, text="Scissors", command=player_scissors).grid(column=1, row=4)
ttk.Button(playerframe, text="Score", command=ask_score).grid(column=1, row=5)
ttk.Button(playerframe, text="Help", command=help).grid(column=1, row=6)

root.mainloop()
#
# while game_running is true:
#     player_throw = ""
#     # comp_throw = random.choice(["rock", "paper", "scissors"])
#     comp_throw = "rock"
#
#     if player_throw == comp_throw:
#         computer_talk.set(f"My {comp_throw} vs. your {player_throw.capitalize()}. We tie!")
#         score[2] += 1
#
#     elif player_throw == "rock":
#         if comp_throw == "scissors":
#             print(f"My {comp_throw} vs. your {player_throw.capitalize()}. You win!")
#             score[1] += 1
#         elif comp_throw == "paper":
#             print(f"My {comp_throw} vs. your {player_throw.capitalize()}. You lose!")
#             score[0] += 1
#
#     elif player_throw == "paper":
#         if comp_throw == "rock":
#             print(f"My {comp_throw} vs. your {player_throw.capitalize()}. You win!")
#             score[1] += 1
#         elif comp_throw == "scissors":
#             print(f"My {comp_throw} vs. your {player_throw.capitalize()}. You lose!")
#             score[0] += 1
#
#     elif player_throw == "scissors":
#         if comp_throw == "paper":
#             print(f"My {comp_throw} vs. your {player_throw.capitalize()}. You win!")
#             score[1] += 1
#         elif comp_throw == "rock":
#             print(f"My {comp_throw} vs. your {player_throw.capitalize()}. You lose!")
#             score[0] += 1
#
#     elif player_throw == "score":
#         print(f"I have won {score[0]}, you have won {score[1]}, and we have tied {score[2]}!")
#
#     elif player_throw == "help":
#         print("Once you start the game, you can choose\n"
#           "rock, paper, or scissors. I will,\n"
#           "also choose one of those at random!\n"
#           "I will go ahead and keep track of our games\n"
#           "and tell you who is the winner if you type,\n"
#           "'score' instead of rock,paper, or scissors!\n "
#           "If you are done playing, then just type in quit\n"
#           "to leave the game. Have fun!\n \n")
#
#     else:
#         if player_throw == "quit":
#             print("Thanks for playing!!!! \n"
#                   "\n"
#                   f"Final Score: \n I won {score[0]}, you won {score[1]}, and we tied {score[2]}! ")
#         else:
#             print("What? Come on, ROCK, PAPER, or SCISSORS!")