def bookie(func):
     func.count += 1
def myfunc():
     bookie(myfunc)
     # Some other code goes here
myfunc.count = 0
for i in range(20):
     myfunc()
print (myfunc.count)
