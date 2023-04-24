import Question

question_prompts=[
    "What color is an apple\n(a) blue\n(b) red\n(c) pirple\n\n",
    "What color is a banana\n(a) blue\n(b) red\n(c) yellow\n\n",
    "What color is an watermellon\n(a) green\n(b) red\n(c) pirple\n\n"
]

questions=[
    Question.Question(question_prompts[0],'b'),
    Question.Question(question_prompts[1],'c'),
    Question.Question(question_prompts[2],'a')
]
result=0
for question in questions:
    print(question.prompt)
    answer=input("Enter answer:")
    if answer==question.answer:
        print("Right answer!\n")
        result+=1
    else:
        print("Wrong answer!\n")
        print()
output="Your total result is {}/{}"
print(output.format(result,len(questions)))


