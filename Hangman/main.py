import random
def find_matches(arr,char):
    result = []
    for i in range(len(arr)):
        if arr[i] == char:
            result.append(i)
    return result
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

words=[
    "universitet",
    "daskalo",
    "pedal",
    "python",
    "anaconda",
    "kopenhagen",
    "yeet",
    "kardibъ"
]
word=random.choice(words)
output=[]
for letter in word:
    output.append("_ ")
count=6
right_count=0
while True:
    print()
    if right_count==len(word):
        for letter in output:
            print(letter , end="")
        print()
        print(colored(0,255,0,"You win!!!"))
        break
    if count==0:
        print(colored(255,0,0,"You lose :("))
        print("Word was",word.capitalize())
        break
    else:
        for letter in output:
            print(letter , end="")
        print()
        print("You have", count, "tries left")
        guess=input("Enter guess:").lower()
        if len(guess)!=1:
            print(colored(255,0,0,"Invalid input"))
            count-=1
        else:
            right_guesses=find_matches(word,guess)
            if len(right_guesses)==0:
                print(colored(255,0,0,"Wrong guess"))
                count-=1
            else:
                for i in right_guesses:
                    output[i]=guess.capitalize() + " "
                right_count = right_count + len(right_guesses)

    



        
        