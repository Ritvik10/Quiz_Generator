from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("500x400")
window.title("QUIZ GENERATOR APPLICATION-RITVIK CHAWLA")
window["bg"]="#660033"

questions_list=[]
choices_list=[]
answers_list=[]
correct_answers=[]
n1=int(input("Number of questions to be taken:"))

for i in range(1,n1):
    print("Enter questions:",i)
    questions_list.insert(i,input())
    print("Enter 4  choices:")
    for j in range(4):
        choices_list.insert(j,input())
    answers_list.insert(i,choices_list)
    print("The correct answers are:")
    print(correct_answers.insert(j,input()))
#for k in range(4):
 #   solution_key.insert(k,input())
#correct_answer.insert(k,solution_key)
#
#
#
#LABEL FOR HEADING
#Label(window,width="400",text="PYTHON QUIZ GENERATOR APPLICATION",bg="#FFFF00",fg="#000000",font='Helvetica 12 bold').pack()
#LABEL FOR QUESTION
#label2=Label(window,text='',textvariable=que,bg="#04112d",fg="#ffffff",font='Helvetica 13 bold')
#label2.place(x=90,y=35)


print("Questions asked are:",questions_list)

print("Answers options as below :",answers_list)
print("Correct answers are:",correct_answers)





    


    
