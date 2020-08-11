import re

strongPW= re.compile(r'''
    (.)(8,)|
    [A-Z]+|
    [a-z]+|
    [0-9]+
    ''')
print('enter your password: ')
passWord=input()

if strongPW.search(passWord)!= None:
    print('this is a strong password')
else:
    print('not strong')
