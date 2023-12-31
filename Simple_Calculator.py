def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    if y!= 0:
        return x/y
    else:
        return "Cannot Divide By Zero"
a = "WELCOME TO SIMPLE CALCULATOR"
b = a.center(50,"-")
print(b,"\n")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
choice = int(input("Enter Your Choice(1-4) : "))
first_num = float(input("Please Enter Your First Number : "))
second_num = float(input("Please Enter Your Second Number : "))
if choice==1:
    print(first_num,"+",second_num,"=",add(first_num,second_num))
elif choice==2:
    print(first_num,"-",second_num,"=",subtract(first_num,second_num))
elif choice==3:
    print(first_num,"x",second_num,"=",multiply(first_num,second_num))
elif choice==4:
    print(first_num,"/",second_num,"=",division(first_num,second_num))
else:
    print("Invalid Choice. Please Try Again")