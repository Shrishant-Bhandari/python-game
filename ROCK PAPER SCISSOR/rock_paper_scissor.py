import random as r

a = r.randint(1,3)

b = int(input("""Enter the number for: 
                                      1. ROCK  
                                      2. PAPER  
                                      3. SCISSOR \n"""))

if a == 1:
    print("Computer Value : ROCK")

elif a == 2:
    print("Computer Value : PAPER")

else:
    print("Computer value : SCISSOR")


if b  > 3 or b < 1:
    print("Invalid input")

elif a == b:
    print("Draw")

elif ((a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1)):
    print("Win")

else:
    print("Lose")