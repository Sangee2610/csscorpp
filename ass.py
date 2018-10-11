# Python version you are using.
print(" Python version you are using.")
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

# current date and time.
import datetime
print("current date:\n",datetime.datetime.now())

#find duplicate
def test_func(listt):
    if len(listt)==len(set(listt)):
        return True
    else:
        return False
print(test_func([1,2,3,4]))
print(test_func([1,2,2,3,4,4]))
print(test_func([5,2,4,5]))

#learning random
import random
print(random.randint(0,8))
print(random.random()*100)
mylist=[2,18,'female','csscorp',20000,'engineer','fresher']
print(random.choice(mylist))
#learning rando with shuffle
from random import shuffle
x = [[i] for i in range(10)]
shuffle(x)
