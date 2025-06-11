#CALUCATOR
import os
def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)
dict={"+":add,"-":subtract,"*":multiply,"/":divide}
def caluculator():
    i=float(input("enter your first number:"))
    start=False
    while not start:
        for s in dict:
            print(s)
        op=input("Which operation you want to perform: ")
        i2=float(input("enter your next number: "))
        result=dict[op](i,i2)
        print(f"{i} {op} {i2} ={result}")
        check=input("ENTER 'c' to continue with the result or to start new calculation enter 'n' and to 'e' to exit: ").lower()
        if check=="c":
            i=result
        elif check=="n":
            start=True
            os.system('cls')
            caluculator()
        else:
            start=True
            print("OK DONE!!")
caluculator()