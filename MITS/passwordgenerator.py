#Password generator
import random
letters=['a','b','c','d','e','f','g','h']
symbols=['@','#','$','%','!']
numb=['1','3','4','5','7']
print("Welcome to the password generator!!")
l=int(input("How many letters you need in your password:"))
print(l)
n=int(input("How many symbols you need:"))
print(n)
s=int(input("How many numbers you need:"))
print(s)
password_list=[]
for i in range(1,l+1):
    char=random.choice(letters)
    password_list += char
for i in range(1,n+1):
    char=random.choice(symbols)
    password_list += char
for i in range(1,s+1):
    char=random.choice(numb)
    password_list += char
print(password_list)
random.shuffle(password_list)
print(password_list)
password =""
for i in password_list:
    password+=i
print(password)