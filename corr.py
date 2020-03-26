import math
a=[15,26,10,9,15,20,18,11,8,20]
b = [103, 79, 91, 99, 110, 95, 101, 108, 112, 102]
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
print ("Age - Score")
print(corr(a,b))