from goto import with_goto
def print_grid(grid):
    print("   |" + "   |" + "   ")
    print(" " + grid[0][0] + " |" + " " + grid[0][1] +" |" + " " +grid[0][2] + " ")
    print("   |" + "   |" + "   ")
    print("‾‾‾"+"|‾‾‾"+"|‾‾‾")
    print(" " + grid[1][0] + " |" + " " + grid[1][1] +" |" + " " +grid[1][2] + " ")
    print("   |" + "   |" + "   ")
    print("‾‾‾"+"|‾‾‾"+"|‾‾‾")
    print(" " + grid[2][0] + " |" + " " + grid[2][1] +" |" + " " +grid[2][2] + " ")
    print("   |" + "   |" + "   ")

def is_grid_full(grid):
    for row in grid:
        for element in row:
            if element==" ":
                return False
    return True

def get_input():
    try:
        return int(input("Player's move: "))
    except:
        print("Enter a number!!!")
        get_input()

def find_winner(grid):
    #checks for row
    if grid[0][0]!=" " and grid[0][0]==grid[0][1]==grid[0][2]:
        if(grid[0][0]=="X"):
            return "Player1"
        else:
            return "Player2"

    elif grid[1][0]!=" " and grid[1][0]==grid[1][1]==grid[1][2]:
        if(grid[1][0]=="X"):
            return "Player1"
        else:
            return "Player2"

    elif grid[2][0]!=" " and grid[2][0]==grid[2][1]==grid[2][2]:
        if(grid[2][0]=="X"):
            return "Player1"
        else:
            return "Player2"

    #checks for cols
    elif grid[0][0]!=" " and grid[0][0]==grid[1][0]==grid[2][0]:
        if(grid[0][0]=="X"):
            return "Player1"
        else:
            return "Player2"

    elif grid[0][1]!=" " and grid[0][1]==grid[1][1]==grid[2][1]:
        if(grid[0][1]=="X"):
            return "Player1"
        else:
            return "Player2"

    elif grid[0][2]!=" " and grid[0][2]==grid[1][2]==grid[2][2]:
        if(grid[0][2]=="X"):
            return "Player1"
        else:
            return "Player2"

    #checks for diagonals
    elif grid[0][0]!=" " and grid[0][0]==grid[1][1]==grid[2][2]:
        if(grid[0][0]=="X"):
            return "Player1"
        else:
            return "Player2"

    elif grid[0][2]!=" " and grid[0][2]==grid[1][1]==grid[2][0]:
        if(grid[0][2]=="X"):
            return "Player1"
        else:
            return "Player2"
    



grid=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

is_game_over=False
winner=None
print_grid(grid)

while is_game_over==False:
    grid_full=is_grid_full(grid)
    if grid_full==True:
        print("Draw")
        break
    
    try:
        player1_input=int(input("Player1's move: "))
    except:
        print("Enter a number!!!")
        player1_input=get_input()

    if player1_input<=3 and player1_input>=0:
        if grid[0][player1_input-1]==" ":
            grid[0][player1_input-1]="X"
        else:
            print("Can't change that")

    elif player1_input>3 and player1_input<=6:
        if grid[1][player1_input-4]==" ":
            grid[1][player1_input-4]="X"
        else:
            print("Can't change that")

    elif player1_input>6 and player1_input<=9:
        if grid[2][player1_input-7]==" ":
            grid[2][player1_input-7]="X"
        else:
            print("Can't change that")

    else:
        print("Invalid input! You must input a number between 1 and 9")

    print()
    print_grid(grid)
    winner=find_winner(grid)
    if winner!=None:
        print("The winner is",winner)
        break

    grid_full=is_grid_full(grid)
    if grid_full==True:
        print("Draw")
        break

    if winner==None:
        try:
            player2_input=int(input("Player2's move: "))
        except:
            print("Enter a number!!!")
            player2_input=get_input()

        if player2_input<=3 and player1_input>=0:
            if grid[0][player2_input-1]==" ":
                grid[0][player2_input-1]="O"
            else:
                print("Can't change that")

        elif player2_input>3 and player2_input<=6:
            if grid[1][player2_input-4]==" ":
                grid[1][player2_input-4]="O"
            else:
                print("Can't change that")

        elif player2_input>6 and player2_input<=9:
            if grid[2][player2_input-7]==" ":
                grid[2][player2_input-7]="O"
            else:
                print("Can't change that")

        else:
            print("Invalid input")

        print()
        print_grid(grid)

    winner=find_winner(grid)
    if winner!=None:
        print("The winner is",winner)
        break
    
        

