# find .txt
# compile text
# print results

import os, re

setPath = r'C:\Users\Desktop'

for findtxt in os.listdir(setPath):
    if findtxt.endwith('txt'):
        txtFile = open(setPath + '\\' +findtxt)
        txtContent = txtFile.read()
        findtxtRegex = re.compile(r'')
