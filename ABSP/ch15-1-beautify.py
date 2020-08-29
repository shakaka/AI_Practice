# stopwatch

import time, pyperclip

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
        lap = 'lap #{}{}({})'.format((str(lapNum)+':').ljust(3),
                                      str(totalTime).rjust(5),
                                      str(lapTime).rjust(6))
        print(lap, end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
        pyperclip.copy(lap)
except KeyboardInterrupt:
    # ctrl-c
    #sys.exit()
    print('\n Done')
