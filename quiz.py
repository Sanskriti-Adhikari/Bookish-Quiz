import csv
import random
quiz_set=[]
with open("questions.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        quiz_dict={
        "question": row["question"],
        "option1": row["option1"],
        "option2": row["option2"],
        "option3": row["option3"],
        "option4": row["option4"],
        "answer": row["answer"]
         }
        quiz_set.append(quiz_dict)
random.shuffle(quiz_set)
print("====================================")
print("        WELCOME TO THE QUIZ!        ")
print("Test your knowledge and have fun!")
print("====================================\n")
score=0
for ques in quiz_set:
    print(ques["question"])
    print("a. "+ques["option1"])
    print("b. "+ques["option2"])
    print("c. "+ques["option3"])
    print("d. "+ques["option4"])
    while True:
        user_answer = input("Enter correct option (A/B/C/D): ").strip().upper()
        if user_answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Enter a valid alphabet")
    if user_answer == "A":
        selected = ques["option1"]
    elif user_answer == "B":
        selected = ques["option2"]
    elif user_answer == "C":
        selected = ques["option3"]
    else:
        selected = ques["option4"]
    if selected == ques["answer"]:
        print("Correct!")
        score+=1
        print(score)
    else:
        print("Wrong!")
        print("Correct ans is "+ques["answer"])
        print(score)
    choice=input("Enter(N/n) to exit and any key to continue: ").upper()
    if choice=="N":
        break 
print("Thank you for playing!")