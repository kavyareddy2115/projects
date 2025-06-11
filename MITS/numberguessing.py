#.NUMBER GUSSEING PROJECT
import random
def easy_level():
    attempts=10
    while attempts<=10:
        print(f"you have {attempts} attempts left to guess")
        guess=int(input("Enter a number between 1-50: "))
        if guess==num:
            print("Correct!!! you won the game")
            break
        elif attempts==1:
            print("OOPS! you have no attempts left,Play again")
            break
        elif guess<1 or guess>50:
            print("It's Out of range...")
            attempts-=1
        elif guess>num:
            print("It's too high")
            attempts-=1
        elif guess<num:
            print("It's too low")
            attempts-=1
def hard_level():
    attempts=5
    while attempts<=5:
        print(f"you have {attempts} left to guess")
        guess=int(input("Enter a number between 1-50: "))
        if guess==num:
            print("Correct!!! you won the game")
            break
        elif attempts==1:
            print("OOPS! you have no attempts left,Play again")
            break
        elif guess<1 or guess>50:
            print("It's Out of range...")
            attempts-=1
        elif guess>num:
            print("It's too high")
            attempts-=1
        elif guess<num:
            print("It's too low")
            attempts-=1
print("Welcome to number guessing game!!")
num=random.randint(1,50)
choose=input("Choose your difficulty level s 'easy' or 'hard': ")
print(choose)
if choose=="easy":
    easy_level()
elif choose=="hard":
    hard_level()
else:
    print("Invalid choise...Try again!!!")
