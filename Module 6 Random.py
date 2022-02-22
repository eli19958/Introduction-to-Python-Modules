
#ELizabeth Motnero
#02/22/22
#Problem 1 randomrange.py


import random
for i in range(10):
    print(random.randrange(25,36))
  #picks out the number        

#Problem 2 randomint.py

import random
print(random.randrange(0,50)*2 +1)

#Problem 3 randomday.py
import random
days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
print(random.choice(days))
#choice was Monday

#Problem 4 pi.py
import math
k = 1

s = 0
for i in range(1000000):

    if i % 2 == 0:
        s += 4/k
    else:
        s -= 4/k
    k += 2
print('Value of estimated pi: '  , s)
print('value of pi from math module: ' ,math.pi)
#to calculate the math.pi

#Problem 5 degrees.py
def Convert(radian):
    pi = 3.14159
    # Simply used the formula
    degree = radian * (180/pi)
    return degree
 
radian = 5
print("degree =",(Convert(radian)))

#Problem 6 factorial.py
import math
n = int(input('Enter an integer:'))
result = 1
for i in range(1, n+1):
    result = result * i
print('factorial of {} using for loop:{}'.format(n, result))
print('factorial of {} using inbuilt function:{}'.format(n, math.factorial(n)))




