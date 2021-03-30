import math
#read file to be string
def readFile(path):
    content = "";
    f = open(path)
    line = f.readline()
    content = content + line
    while line:
        line = f.readline()
        content = content + line
    return content.strip();
#parse string to be array of float
def data(content):
    features = []
    count = 0
    datalist = content.split('\n')
    for i in datalist:
        v = i.strip().split(' ')
        features.append([])
        features[count].append(float(v[0]))
        features[count].append(float(v[1]))
        features[count].append(float(v[2]))
        count = count + 1    
    return features;
#print list for testing
def printer(features):
    for i in features:
        li = i
        for j in li:
            print(str(j) + ", ", end='')
        print()
    return;
#use given parameters for testing data
def testData(testData, parameters):
    totalLoss = 0.0
    for i in testData:
        totalLoss = totalLoss + math.pow((parameters[0] * i[0] + parameters[1] * i[1] + parameters[2] - i[2]), 2)
    print("testing data: \t" + str(totalLoss));
    return;
#linear regression
def SGD(features, learnrate, parameters, flag):
    for i in features:
        gradient = parameters[0] * i[0] + parameters[1] * i[1] + parameters[2] - i[2]
        parameters[0] = parameters[0] - learnrate * gradient * i[0]
        parameters[1] = parameters[1] - learnrate * gradient * i[1]
        parameters[2] = parameters[2] - learnrate * gradient
    totalLoss = 0.0
    for i in features:
        totalLoss = totalLoss + math.pow((parameters[0] * i[0] + parameters[1] * i[1] + parameters[2] - i[2]), 2)
    if flag == 1:
        print(str(parameters[0]) + " " + str(parameters[1]) + " " + str(parameters[2]))
        print("totalLoss:" + str(totalLoss))
        path = "dataForTesting.txt"
        content = readFile(path)
        test = data(content)
        testData(test, parameters)
    return;
	
#running
path = "dataForTraining.txt"
content = readFile(path)
features = data(content)
#printer(features)
parameters = [0.0, 0.0, 0.0]
learnrate = 0.0002
i = 0
while i < 5000:
    flag = 0
    if i % 200 == 0:
        flag = 1
    SGD(features, learnrate, parameters, flag)
    i = i + 1



