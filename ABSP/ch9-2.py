# find big files and delete it

import os

def findFileSize(filePath, fileSize):
    for foldername, subfolders, filenames in os.walk(filePath):
        for myFile in filenames:
            if os.path.getsize(os.path.join(foldername,myFile))>fileSize:
                print(os.path.join(foldername,myFile))

findFileSize()
