from termcolor import colored

input=int(input("Enter side of square: "))
for i in range(input):
    for j in range(input):
        if j==i or j==input-1-i:
            print("*",end="")
        else:
            print(colored("*","blue"),end="")

    print()
    