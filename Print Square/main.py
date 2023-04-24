
input=int(input("Enter a number: "))
first_row="╔"+"═"*(input-2)+"╗"
last_row="╚" + "═"*(input-2) + "╝"
print(first_row)
for i in range(input):
    print("║",end="")
    for j in range(input-2):
        print(" ",end="")
    print("║")
print(last_row)
    