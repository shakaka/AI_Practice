import os, shutil, time, datetime

thePath = 'D:\py_workspace\changedName'
newPath = 'D:\py_workspace\changedName\withDate'

shutil.copy('D:\py_workspace\changedName\changedName.py','D:\py_workspace\changedName\withDate')

#timestr = time.strftime('%Y-%m-%d-%H%M%S')
fileName = r'D:\py_workspace\changedName\withDate\Ulog_%s.py'%datetime.datetime.now()

os.rename('D:\py_workspace\changedName\withDate\changedName.py',fileName)
