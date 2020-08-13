#! python3
# backupToZip

import os, zipfile

def backupToZip(folder):
    # backup the entire contents of folder to zip
    folder = os.path.abspath(folder) #absolute folder
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' +str(number) +'.zip'
        if not os.path.exists(zipFileName):
            break
        number +=1
    # create zip
    print('create %s...' %(zipFileName))
    backupZip=zipfile.ZipFile(zipFileName,'w')

    # walk the entire folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('add file in %s...' %(foldername))
        backupZip.write(foldername)

        # add all files to zip
        for filename in filenames:
            newBase = os.path.basename(folder) +'_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't back up the backup zip file
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
    print('done')

backupToZip('C:\\*')
