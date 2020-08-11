import re

haRex= re.compile(r'(ha){3}')
mo1=haRex.search('hahahahaaa')
mo1.group()
mo1==None
mo2=haRex.search('hahaha')
mo2.group()
