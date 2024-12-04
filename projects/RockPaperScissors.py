import random
import time


# PLAN
# create rps options
# playRound
# Ask for input
# Check validity of input
# Generate random num from 1-3
# Choose rps option based on number
# Check winner
# If winner -> print the winner
# Else -> recurse

class RPSOption:
    def __init__(self, wins, loses):
        self.__wins = wins
        self.__loses = loses

    def wins_against(self, option):
        return self.__wins == option

    def loses_to(self, option):
        return self.__loses == option


class Rock(RPSOption):
    def __init__(self):
        super().__init__("scissors", "paper")


class Paper(RPSOption):
    def __init__(self):
        super().__init__("rock", "scissors")


class Scissors(RPSOption):
    def __init__(self):
        super().__init__("paper", "rock")

def play_round():
    user_input = input("[Game] Choose rock, paper or scissors!\n>>> ")
    user_input = user_input.lower()

    if user_input == "rock":
        print("[Game] You chose Rock!")
    elif user_input == "paper":
        print("[Game] You chose Paper!")
    elif user_input == "scissors":
        print("[Game] You chose Scissors!")
    else:
        return print("[Game] Invalid input! You lose!")

    computer_choice: RPSOption | None = None
    random_num = random.randint(1, 3)

    print("[Game] The Computer is choosing...")
    time.sleep(2)

    if random_num == 1:
        print("[Game] The Computer chose Rock!")
        computer_choice = Rock()
    elif random_num == 2:
        print("[Game] The Computer chose Paper!")
        computer_choice = Paper()
    elif random_num == 3:
        print("[Game] The Computer chose Scissors!")
        computer_choice = Scissors()

    time.sleep(2)

    if computer_choice.wins_against(user_input):
        return print("[Game] You lose!")
    elif computer_choice.loses_to(user_input):
        return print("[Game] You win!")
    else:
        print("[Game] Game was a draw, go again!")
        time.sleep(1)
        return play_round()

play_round()