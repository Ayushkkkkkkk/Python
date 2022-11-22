import random


def winner(user, computer):
    user_win_count = 0;
    computer_win_count = 0
    wanna_play = True
    while wanna_play:
        # user setup
        if user == "rock" and computer == "rock":
            print("draw")
        elif user == "paper" and computer == "paper":
            print("draw")
        elif user == "scissor" and computer == "scissor":
            print("draw")

        elif user == "rock" and computer == "paper":
            print("user won")
            user_win_count += 1
        elif user == "rock" and computer == "scissor":
            print("user won")
            user_win_count += 1
        elif user=="scissor" and computer =="paper":
            print("user won ")
            user_win_count +=1


        elif user=="paper" and computer=="rock":
            print("user won")
            user_win_count+=1
        #     computer setup

        elif computer == "rock" and user == "paper":
            print("computer won")
            computer_win_count += 1
        elif computer == "rock" and user == "paper":
            print("user won")
            user_win_count += 1
        wanna_play = False



choices = ["rock", "paper", "scissor"]
user_choice = input("Enter your choice :")
computer_choice = random.choice(choices)
print(f"computer choice is {computer_choice}")
winner(user_choice, computer_choice)
