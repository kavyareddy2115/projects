#encryption and decryption 
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key): 
        cipher_text=""
        for letter in plain_text:
            if letter in a:
                position=a.index(letter)
                new_position=(position+shift_key)%26
                cipher_text+=a[new_position]  
            else:
                 cipher_text+=letter
        print(f"here's the encrypted result:{cipher_text}") 

def decryption(cipher_text,shift_key):
        plain_text=""
        for letter in cipher_text:
            if letter in a:
                position=a.index(letter)
                new_position=(position-shift_key)%26
                plain_text+=a[new_position]
            else:
                 plain_text+=letter
        print(f"here's the decrypted result:{plain_text}")
end=False
while not end:
    i=input("Type 'encrypt' for encryption and 'decrypt' for decryption:\n")
    n=input("Type your message:\n").lower()
    s=int(input("Type the shift number:\n"))
    if i=="encrypt":
        encryption(plain_text=n,shift_key=s)
    elif i=="decrypt":
        decryption(cipher_text=n,shift_key=s)
    again=input("Type 'yes'to continue,or 'no' to stop:")
    if again=='no':
         end=True
         print("bye")