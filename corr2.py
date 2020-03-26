import math
a = [20,30,40,50,60]
b = [32,36,38,36,32]
def mean(x):
    sum = 0.0
    for i in x:
         sum += i
    return sum / len(x) 
    
def StandardDeviation(x):
    sumv = 0.0
    for i in x:
         sumv += (i - mean(x))**2
    return math.sqrt(sumv/(len(x)-1))

def corr(x, y):
    scorex = []
    scorey = []
    for i in x: 
        scorex.append((i - mean(x))/StandardDeviation(x)) 
    for j in y:
        scorey.append((j - mean(y))/StandardDeviation(y))   
    return (sum([i*j for i,j in zip(scorex,scorey)]))/(len(x)-1)
print ("Miles/Hour - Miles/Gallon")
print(corr(a,b))