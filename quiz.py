Questions={
    "What is the Capital of France?":"Paris",
    "What is sum of this number 2+2 ?":"4",
    "Give The Ans of this Expression 2+2-4+6?":"6"
}


total_question=len(Questions);
score=0
print("Welcome To The Quiz Game \n")
print("Enter 'Quit' to Stop Game \n")

for question,correct_ans in Questions.items():
    user_answer=input(question + "")
    if user_answer.lower() =="quit":
        break;  #exit the loop
    elif user_answer.lower()==correct_ans.lower():
        print("Correct!")
        score+=1
    else:
        print(f"Wrong! The Correct Answer is {correct_ans}")

print()

print(f"Quiz Completed. Your Score is {score}\{total_question}") 

   

