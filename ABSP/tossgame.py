import random
def inputGuess():
    guess = ""
    while guess not in ("heads", "tails"):
        guess = input("Guess the coin toss! Enter heads or tails:")
    return guess
def autoToss():
    toss = random.randint(0, 1)
    if toss == 0:
        toss = "tails"
    else:
        toss = "heads"
    return toss
guess = inputGuess()
toss = autoToss()
if toss == guess:
    print("You got it!")
else:
    print("Nope! Guess again!")
    guess = inputGuess()
    toss = autoToss()
    if toss == guess:
        print("You got it!")
    else:
        print("Nope. You are really bad at this game.")
