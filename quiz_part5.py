enter_your_choice="Enter your choice:"
score=0
question="""ART AND LITERATURE: Who painted Starry Night?
a. Vincent van Gogh
b. Michelangelo
c. Leonardo da Vinci
"""
choice=input(question+enter_your_choice)
if choice=="a":
    print("Correct!")
    score+=1
else:
    print("The correct answer was a")

question="""ENTERTAINMENT: How many oscars did Alfred Hitchcock win?
a. None
b. One
c. Two
"""
choice=input(question+enter_your_choice)
if choice=="a":
    print("Correct!")
    score+=1
else:
    print("The correct answer was a")

question="""GEOGRAPHY: Which is the largest ocean?
a. Pacific
b. Atlantic
c. Indian
"""
choice=input(question+enter_your_choice)
if choice=="a":
    print("Correct!")
    score+=1
else:
    print("The correct answer was a")

question="""HISTORY: Who was the first U.S. president to appear on a coin?
a. Washington
b. Lincoln
c. Jefferson
"""
choice=input(question+enter_your_choice)
if choice=="b":
    print("Correct!")
    score+=1
else:
    print("The correct answer was b")

question="""SCIENCE AND NATURE: Can pigs swim?
a. Yes
b. No
c. Only in salt water
"""
choice=input(question+enter_your_choice)
if choice=="a":
    print("Correct!")
    score+=1
else:
    print("The correct answer was a")

question="""SPORT AND LEISURE: What color is the middle Olympic ring?
a. Red
b. Blue
c. Black
"""
choice=input(question+enter_your_choice)
if choice=="c":
    print("Correct!")
    score+=1
else:
    print("The correct answer was c")

question="""GENIUS: What is D divided by X?
"""
choice=input(question+"Enter your answer:")
if choice=="L" or choice=="50":
    print("Correct!")
    score+=1
else:
    print("Correct answers were L or 50")

score=str(score)
print("Your final score is",score)

score=float(score)
if score >=0 and score <=2:
    print("You were unlucky!")
elif score >=3 and score <=4:
    print("You did better than chance!")
elif score >=5 and score <=6:
    print("You are a trivia star!")
else:
    print("Genius!")
