import random
print("welcome to the guess game if you guess the number under 5 times you win or else you lose" )
print("**********")
randNumber = random.randint(1,20)
userguess = None
guesses = 0
while(userguess != randNumber):
    userguess = int(input("enter the guess : "))
    guesses += 1
    if(userguess == randNumber):
        print("you guess the right number")
    else:
        if(userguess > randNumber):
            print("wrong guess ! please input shorter number")
        else:
            print("wrong guess ! please input greater number")
print(f"so you completed the guess in {guesses} guesses")
if(guesses <= 5):
    print("congrats you won for getting in winning criteria")
else:
    print("you guessed it right but you have cross the winning criteria")

