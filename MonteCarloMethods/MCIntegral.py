import cmath
import math
import random

#function
def mean(plist):
    s = 0
    for i in range(len(plist)):
        s = s + plist[i]
    s = s / len(plist)
    return s;

def deviation(m, plist):
    s = 0
    for i in range(len(plist)):        
        s = s + (plist[i] - m)*(plist[i] - m)
    s = s / len(plist)
    return s;


def distance(x0, y0, x1, y1):
    s = 0;
    s = (x1 - x0) * (x1 - x0) + (y1 - y0)*(y1 - y0)
    s = cmath.sqrt(s)
    return s;

def estimatePI(N):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    count = 0;
    for i in range(N):
        x1 = random.random()
        y1 = random.random()
        dis = distance(x0, y0, x1, y1)
        if dis.real <= 1:
            count = count + 1
    #pi estimate
    estimate = count/N * 4
    return estimate;

def estimateIntegral(N):
    x0 = 0
    y0 = 0
    count = 0
    for i in range(N):
        x0 = random.random()
        y0 = random.random()
        y = x0 * x0 * x0
        if y0 <= y:
            count = count + 1
    #integral estimate
    estimate = count/N
    return estimate;

def function(x, y):
    f = 0
    f1 = math.pow(y, 2)
    f2 = math.pow(math.e, -f1)
    f3 = x
    f4 = math.pow(math.e, -math.pow(x, 2))
    f5 = f3 * f4
    f6 = math.pow(x, 3)
    f = f1 * f2 / f5
    f = f + f6
    return f;

def estimateDIntegral(N):
    a = 2
    b = 4
    c = -1
    d = 1
    h1 = math.pow(math.e, 15)/4 + 64
    h2 = 8
    height = h1 - h2
    volume = (b - a) * (d - c) * height
    x0 = 0
    y0 = 0
    h = 0
    count = 0
    for i in range(N):
        x0 = (b - a) * random.random() + a
        y0 = (d - c) * random.random() + c
        h = height * random.random() + h2
        f = function(x0, y0)
        if h <= f:
            count = count + 1
    estimate = count/N
    estimate = estimate * volume
    return estimate;




#running code

print("Estimate PI")
piList = []
times = [20, 50, 100, 200, 300, 500, 1000, 5000]
for n in times:
    print(n, " \ttimes sampling:")
    for i in range(20):
        estimate = estimatePI(n)
        piList.append(estimate)
    #print(piList)
    m = mean(piList)
    d = deviation(m, piList)
    print("mean: \t\t", m)
    print("deviation: \t", d)
    piList = []

print()
print("Estimate the integral of x^3")
piList = []
times = [5, 10, 20, 30, 40, 50, 60, 70, 80, 100]
for n in times:
    print(n, " \ttimes sampling:")
    for i in range(100):
        estimate = estimateIntegral(n)
        piList.append(estimate)
    #print(piList)
    m = mean(piList)
    d = deviation(m, piList)
    print("mean: \t\t", m)
    print("deviation: \t", d)
    piList = []

print()
print("Estimate the double integral of (y^2 * e^(-y^2) + x^4 * e^(-x^2))/(x * e^(-x^2))")
piList = []
times = [10, 20, 30, 40, 50, 60, 70, 80, 100, 200, 500]
for n in times:
    print(n, " \ttimes sampling:")
    for i in range(100):
        estimate = estimateDIntegral(n)
        piList.append(estimate)
    print(piList)
    m = mean(piList)
    d = deviation(m, piList)
    print("mean: \t\t", m)
    print("deviation: \t", d)
    piList = []



















    


