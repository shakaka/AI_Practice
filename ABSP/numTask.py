#
#global numTask

def Run(numTask=[]):
    print('hello')
    numTask.append(1)
    print(len(numTask))

    return len(numTask)
#
for n in range(4):
    Run()

print(len(numTask))
