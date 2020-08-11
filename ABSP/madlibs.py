# adjective noun adverb verb

import os, re

madLibs = open(os.path.abspath('.')+'\\madlibs.txt','r') #read text
originalText=madLibs.read()
madLibs.close()

originalRegex=re.compile(r'ADJECTIVE|NOUN|SADVERB|VERB')
originalMatch=originalRegex.findall(originalText)
answer=[]

for i in originalMatch():
    if i == 'ADJECTIVE':
        answer.append(input('enter an adjective: '))
    elif i == 'NOUN':
        answer.append(input('enter a noun: '))S
    elif i == 'ADVERB':
        answer.append(input('enter an adverb:'))
    elif i == 'VERB':
        answer.append(input('enter a verb: '))

changeMatch=originalRegex.sub(r'%s',originalText)
answerText=changeMatch%tuple(answer)
print(answerText)
newMadlibs=open('New mad libs.txt','w')
newMadlibs.write(answerText)
newMadlibs.close()
