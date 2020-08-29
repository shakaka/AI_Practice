import os, time

filepath = 'D:\py_workspace\changedName\withDate'
if not os.path.exists(filepath):
    os.mkdir(filepath)
timestr = time.strftime('%Y-%m-%d-%H%M%S')
fileNum = 'Log_'+str(timestr)+'.txt')
with open(os.path.join(filepath, fileNum),'w+') as file:
    file.write('')
file.close()

with open(fileNum,'w') as fo:
    fo.write("you can try this.")
fo.close()
