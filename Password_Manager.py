import random
import string

pwd= {} #Empty Dict

#Load File
try:
    with open("password.txt","r") as f:
        for line in f:
            key, value= line.strip().split(" : ") #WEBSITE is Key & PASSWORD is Value
            pwd[key]= value #Saved in Dict
except FileNotFoundError:
    pass

def gen_password(x):
    char= string.ascii_letters + string.digits + string.punctuation
    p= "".join(random.choice(char) for i in range(x))
    return p

#User Input
while True:
    print("\n-----PERSONAL PASSWORD MANAGER-----\n")
    print("1. Add New Password")
    print("2. View Your Passwords")
    print("3. Exit")
    
    c= input("Enter Choice: ") #Choice of USER
    
    if c=="1":
        web= input("Enter Website: ")
        if web in pwd:
                print("Password Already Exists For This Website!")
                continue
        try:
            length= int(input("Enter Length Of Password: "))
        except ValueError:
            print("Enter A Valid Number: ")
            continue
        if length<6:
            print("Password Length Should Be Minimum 6 Characters!")
            continue
        password= gen_password(length) #Generated Password
        pwd[web]= password #Saved in Dict
        print(f"{web} Password is : {password}")

    elif c=="2":
        if not pwd:
            print("No Data Stored!")
        else:
            print("\nYOUR SAVED PASSWORDS\n")
            for key in sorted(pwd):
                print(f"{key} : {pwd[key]}") #Print Dict

    elif c=="3":
        with open("password.txt","w") as f:
            for key, value in pwd.items():
                f.write(f"{key} : {value}\n") #Saved in File
        print("Exiting......")
        print("Passwords Saved To password.txt")
        print("Congrats! You Successfully Used Personal Password Manager.")
        break

    else:
        print("Invalid Choice! Please try again.")