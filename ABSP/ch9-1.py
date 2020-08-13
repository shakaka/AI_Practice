# copy file to a new folder

import os, shutil, re

def lookForFile(filePath, newPath, fileType):
#loof for .pdf
    number = 1
    while True:
        copyFileFolder = newPath + '_' +str(number)
        if not os.path.exists(copyFileFolder):
            break
        number +=1
    os.makedirs(copyFileFolder)
    for foldername, subfolders, filenames in os.walk(file):
        for selectFile in filenames:
            if selectFile.endswith(fileType):
                shutil.copy(os.path.join(foldername,selectFile),copyFileFolder)

lookForFile()
