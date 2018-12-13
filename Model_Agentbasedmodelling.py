#import modules
import random


#make variables random integer between inc 0-99
y0 = random.randint(0,99)
x0 = random.randint(0,99)
print (y0)
print (x0)


#randomly move variables 1 step
if random.random() < 0.5:
    y0 = y0+1
else:
    y0 = y0-1
if random.random() <0.5:
    x0 = x0+1
else:
    x0 = x0-1

    
print(y0, x0)


#move y0 and x0 variables a second step
if random.random() < 0.5:
    y0 = y0+1
else:
    y0 = y0-1
if random.random() <0.5:
    x0 = x0+1
else:
    x0 = x0-1

    
print(y0, x0)    












#make second set of variables
y1 = random.randint(0,99)
x1 = random.randint(0,99)
print (y1)
print (x1)


#randomly move y1 and x1 variables 1 step
if random.random() < 0.5:
    y1 = y1+1
else:
    y1 = y1-1
if random.random() <0.5:
    x1 = x1+1
else:
    x1 = x1-1

    
print(y1, x1)


#move variables a second step
if random.random() < 0.5:
    y1 = y1+1
else:
    y1 = y1-1
if random.random() <0.5:
    x1 = x1+1
else:
    x1 = x1-1

    
print(y1, x1)

#calculate euclidean distance between y0,x0 and y1,x1
answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print(answer)    



