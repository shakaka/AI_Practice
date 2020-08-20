# remove csv header

import csv, os

os.makedirs('headRemoved',exist_ok=Ture)

#loop through every file in the folder
for csvFileName in os.listdir('.'):
    if not csvFileName.endswith('.csv'):
        continue #skip non-csv files
    print('removing header from ' + csvFileName +'...')
#read csv file
csvRows = []
csvFileObj = open(csvFileName)
readerObj = csv.reader(csvFileObj)

for row in readerObj:
    if readerObj.line_num == 1:
        continue #skip the firest line
    csvRows.append(row)
csvFileObj.close()

#write out the file
csvFileObj = open(os.path.join('headerRemoved',csvFileName),'w',
             newline='')
csvWriter = csv.writer(csvFileObj)

for row in csvRows:
    csvWriter.writerow(row)
csvFileObj.close()
