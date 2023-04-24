import random
def find_winner(computer,player):
    if player=="rock":
        if computer=="paper":
            return "computer"
        elif computer=="scissors":
            return "player"
    elif player=="paper":
        if computer=="scissors":
            return "computer"
        elif computer=="rock":
            return "player"
    elif player=="scissors":
        if computer=="paper":
            return "player"
        elif computer=="rock":
            return "computer"

options=["rock","paper","scissors"]
player_input=input("Enter your play:")
computer_input=random.choice(options)
has_winner=False

while has_winner==False:
    if player_input==computer_input:
        print("\nDraw")
        player_input=input("Enter your play:")
        computer_input=random.choice(options)

    elif player_input in options:
        winner=find_winner(computer_input,player_input)

        if winner=="computer":
            print("\nComputer's choice was",computer_input)
            has_winner=True
            print("You lose")

        if winner=="player":
            print("\nComputer's choice was",computer_input)
            has_winner=True
            print("You win")
            
    else:
        print("Invalid output")
        player_input=input("Enter your play:")
        computer_input=random.choice(options)
