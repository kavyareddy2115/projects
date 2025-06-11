#ROCK PAPER SCISSORS
import random
select=[0,1,2]
computer_choice=random.choice(select)
users_choice=int(input("what do you want to select?\n 0/ROCK\n 1/PAPER\n 2/SCISSOR\n"))
print("COMPUTERS CHOICE IS ",computer_choice)
print("USEERS CHOICE IS ",users_choice)
if(users_choice<0 and users_choice>2):
    print("Invalid choice,try again")
if(users_choice==computer_choice):
    print("It's a draw")
elif(users_choice==0 and computer_choice==2):
    print("hooo!!you got a point")
elif(users_choice==2 and computer_choice==0):
    print("you lost ,try again")
elif(computer_choice>users_choice):
    print("you lose,try again")
else:
    print("you win")