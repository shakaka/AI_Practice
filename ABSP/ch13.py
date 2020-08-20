# find all pdf and merge

import PyPDF2, os

# get all pdf
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.pdffilewriter()

#loop through all pdf
for filename in pdfFiles:
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.pdffilereader(pdfFileObj)
    #loop through all pages
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#save the result
pdfOutput = open('allminutes.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
