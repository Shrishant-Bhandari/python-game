import random as r
cond = True 

win = 0 
lose = 0 
draw = 0 

while cond :
    comp = r.randint(1,3)
    try:
        user = int(input("""Enter the number : 
                                           1. ROCK
                                           2. PAPER
                                           3. SCISSOR \n"""))
    
    except ValueError:
        print("You fool!! Go and Enroll in 4th std english class")
        exit()

    if comp == 1:
        print("COMPUTER CHOICE : ROCK")

    elif comp == 2:
        print("COMPUTER CHOICE : PAPER")

    else:
        print("COMPUTER CHOICE : SCISSOR")

    if user < 1 or user > 3:
        print("Invalid Input")

    elif user == comp:
        draw += 1
        print("DRAW")
    
    elif ((comp == 1 and user == 3) or (comp == 2 and user == 1) or (comp == 3 and user == 2)):
        lose += 1 
        print("You lost")
    else :
        win += 1 
        print("You Won")

    print("--------------SUMMARY--------------")
    print("WIN :",win)
    print("LOST :",lose)
    print("DRAW :", draw)


    ch = input("Do you want to continue [y/n]").lower()

    if ch == "y":
        cond = True
    elif ch == "n":
        cond = False
    else :
        print("what a fool man don't you understand the english!!")
        cond = None

print("MADE WITH LOVE BY SHRISHANT")