text = "Number Guessing Game"
print(text)

text = "Guess a number (between 1 and 9):"
print(text)

guess = int(input("enter your guess : "))
if(guess<3):
    print("your guess was too low: Guess a number higher than 3")

guess = int(input("enter your guess : "))
if(guess<7):
    print("your guess was too low: Guess a number higher than 7")

guess = int(input("enter your guess : "))
if(guess==9):
    print("Congratulations YOU WIN!!!")