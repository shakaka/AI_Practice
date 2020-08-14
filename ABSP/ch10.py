# debug the coin game

import random

guess = ''
while guess not in ('heads','tails'):
    print('guess the coin toss! enter heads or tails: ')
    guess = input()
toss = random.randint(0,1) # 0 for tails
if toss == 0:
    toss == 'tails'
    #print('you got it')
else:
    toss == 'heads'
    #print('nope! guess again')
if toss == guess :
    print('you got it')
else:
    print('nope! guess again')
    guess = input()
    if toss == guess:
        print('that is it')
    else:
        print('nope. loser')
