import random
print("------------WELCOME TO ROCK PAPER SCISSORS GAME------------")
print()
usr_score = 0
comp_score = 0
ties = 0
name = str(input("Enter Your Name : "))
print("""
Winnning Rules :
   Rock Vs Scissor ---> Rock
   Paper Vs Rock ---> Paper
   Scissors Vs Paper  ---> Scissors """)
while True:
    print("""
Choices Are : 
  1).Rock
  2).Paper
  3).Scissors""")
    choice = int(input("Enter Your Choice(1-3) : "))
    print()
    if choice == 1:
        usr_choice = "Rock"
    elif choice == 2:
        usr_choice = "Paper"
    elif choice == 3:
        usr_choice = "Scissors"
    else:
        print("Invalid Choice. Please Try Again")
        continue
    computer = random.randint(1,3)
    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"
    print(name,"Choice :",usr_choice,"|","Computer Choice :",comp_choice)
    if(usr_choice == "Rock" and comp_choice == "Scissors") or (usr_choice == "Scissors" and comp_choice == "Rock"):
        result = "Rock"
    elif(usr_choice == "Paper" and comp_choice == "Rock") or (usr_choice == "Rock" and comp_choice == "Paper"):
        result = "Paper"
    elif(usr_choice == comp_choice):
        result = "Tie"
    else:
        result = "Scissors"
    if result == "Tie":
        print()
        print("---- it's a Tie ----")
        ties += 1
    elif result == usr_choice:
        print()
        print("---- You Win ----")
        usr_score += 1
    else:
        print()
        print("---- Computer Win ----")
        comp_score += 1
    print()
    print("Scores Are : ")
    print("--------------------------------------------------")
    print(" "*4 + name,":",usr_score,"|","Computer :",comp_score,"|","Ties Are :",ties)
    print("--------------------------------------------------")
    print()
    repeat = str(input("do you want to play again Yes/No :"))
    if repeat == "No" or repeat == "no":
        break
print()
if usr_score > comp_score:
    print(name,"Win With",usr_score,"Points!")
elif usr_score < comp_score:
    print("Computer Win With",comp_score,"Points!")
else:
    print("It's a Tie! You Both Win With",ties,"Points")
print()
