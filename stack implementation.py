def Push(student):
    h=input("enter your name:")
    student.append(h)
    
def Pop(student):
    if len(student)==0:
        print("Stack is Empty")
    else:
            print("The Removed Element is:", student.pop())

def Display(student):

    print(student)
student=[]
print("Welcome to the Programme of PUSH,POP and Display")
while True:
    print("Enter your Choice:\nEnter 1 for Push:\n Enter 2 for POP:\n Enter 3 for Display:\n Enter 4 for Exit:")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        Push(student)
    elif ch==2:
        Pop(student)
    elif ch==3:
        Display(student)
    elif ch==4:
            print("Thank you for using this Programme\nPlease give your feedback from 1-5:")
            s=int(input("Enter your feedback"))
            print("Your Feedback is",s)
            break
    else:
        print("Sorry for the inconvienience caused")
print("GOODBYE")
                    
