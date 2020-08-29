# a simple countdown script

import time, subprocess

timeleft = 60
while timeleft > 60 :
    print(timeleft, end='')
    time.sleep(1)
    timeleft=timeleft-1

# at the end of counting, play a sound flie
subprocess.Popen(['start','alarm.wav'],shell=True)
