import random as r 

a = r.randint(1,5)

b = int(input("Enter any number between 1 to 5 :"))

if b > a :
    print(a)
    print("Your number is greater")

elif b < a :
    print(a)
    print("your number is smaller")

else:
    print(a)
    print("Aww we predict same number")
