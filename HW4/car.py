Price=42500
print("Guess the price and win the prize!")
i=0
while i<5:
    Guess=int(input("Enter your guess:"))
    if i==4:
        if Guess==Price:
            print("You won!")
        else:
            if Guess<Price:
                print("Too low!")
            if Guess>Price:
                print("Too high!")
            print("You lost!")
    elif Guess==Price:
        print("You won!")
        break
    elif Guess<Price:
        print("Too low!")
    elif Guess>Price:
        print("Too high!")
    i+=1
