import string
import random
weak_password = string.ascii_lowercase
moderate_password = string.ascii_lowercase+string.ascii_uppercase+string.digits
strong_password = string.ascii_letters+string.digits+string.punctuation
while True:
    a = "WELCOME TO THE PASSWORD GENERATOR"
    b = a.center(50,"-")
    print(b,"\n")
    print("1.Generate A New Password")
    print("2.Exit")
    x = int(input("Enter Your Choice(1-2) : "))
    if x==1:
        length = int(input("Please Enter The Length Of Password : "))
        print("Select Password Complexity :")
        print(" " + "1.Weak")
        print(" " + "2.Moderate")
        print(" " + "3.Strong")
        complexity_user = int(input("Enter Your Choice(1-3) : "))
        if complexity_user==1:
            password = "".join(random.choices(weak_password,k=length))
            print("The Generated Password Is : ")
            print(password,"\n")
            q = input("<--Press Enter-->")
            continue
        elif complexity_user==2:
            password1 = "".join(random.choices(moderate_password,k=length))
            print("The Generated Password Is : ")
            print(password1,"\n")
            q = input("<--Press Enter-->")
            continue
        elif complexity_user==3:
            password2 = "".join(random.choices(strong_password,k=length))
            print("The Generated Password Is : ")
            print(password2,"\n")
            q = input("<--Press Enter-->")
            continue
        else:
            print("Invalid Choice. Please Try Again")
            q = input("<--Press Enter-->")
            continue
    elif x==2:
        print("Thanks For Using")
        break
    else:
        print("Invalid Choice. Please Try Again")
        q = input("<--Press Enter-->")
        continue
