# stopwatch

import time, sys

print('press ENTER to start, press ENTER for one turn, press Ctrl-C to quit')

input()
print('started')
startTime = time.time()
lastTime = startTime
lapNum = 1

# tracking lap time
try:
    while True:
        input()
        lapTime = round(time.time()-lastTime,2)
        totalTime = round(time.time()-startTime,2)
        print('lap #%s: %s (%s)' %(lapNum,totalTime,lapTime),end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except keyboardInterrupt:
    # ctrl-c
    sys.exit()
    print('\n Done')
