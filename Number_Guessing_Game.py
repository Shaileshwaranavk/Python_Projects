import random
x = random.randint(1,100)
while True:
    y = int(input("Enter your Guess : "))
    if x == y :
        print("Your Guessing is Right!!!")
        break
    elif x < y :
        print("Lower")
    else:
        print("Higher")