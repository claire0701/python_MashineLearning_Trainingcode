# Autor: Jie Hou 
# Traning Code from book Machine Learing in Python
import sys
import numpy as np
import matplotlib 
import scipy.stats as stats


with open("/Users/Pinguhu/Developer/python/Daten/sonar.all-data.txt") as file:
    lines = file.readlines()

xList =[]
labels = []

for line in lines:
    row = line.strip().split(",")
    xList.append(row)

nrow = len(xList)
ncol = len(xList[1])

type = [0]*3
colCounts = []

for col in range(ncol):
    for row in xList:
        try:
            a = float(row[col])
            if isinstance(a, float):
                type[0] += 1
        except ValueError:
            if len(row[col]) > 0:
                type[1] += 1
            else:
                type[2] += 1
    colCounts.append(type)
    type = [0]*3

""" sys.stdout.write("Col#" + '\t' + "Number" + '\t' +
                "Strings" + '\t' + "Other\n")
iCol = 0 
for types in colCounts:
    sys.stdout.write(str(iCol) + '\t\t' + str(types[0]) + '\t\t' + 
                    str(types[1]) + '\t\t' + str(types[2]) + "\n")
    iCol +=1 """

# generate summary statistics for column 3
col = 3
colData = []
for row in xList:
    colData.append(float(row[col]))

colArray = np.array(colData)
colMean = np.mean(colArray)
colsd = np.std(colArray)
sys.stdout.write("Mean = " + '\t' + str(colMean) + '\t\t' +
                "Standard Deviation = " + '\t' + str(colsd))
stats.probplot(colData, dist="norm", plot=pylab)
pylab.show()

ntiles = 4
percentBdry = []

for i in range(ntiles + 1):
    percentBdry.append(np.percentile(colArray, i*(100)/ntiles))
sys.stdout.write("\nBoundaries for 4 Equal Percentiles \n")
print(percentBdry)
sys.stdout.write(" \n")

#run again with 10 equal intervals
ntiles = 10 
percentBdry = []

for i in range(ntiles + 1):
    percentBdry.append(np.percentile(colArray, i * (100) / ntiles))
sys.stdout.write("\nBoundaries for 10 Equal Percentiles \n")
print(percentBdry)
sys.stdout.write(" \n")

# The last column contains categorical variables

col = 60
colData = []
for row in xList:
    colData.append(row[col])
unique = set(colData)
sys.stdout.write("Unique Label Values \n")
print(unique)

#count up the number of elements having each value
catDict = dict(zip(list(unique), range(len(unique))))
catCount = [0]*2

for elt in colData:
    catCount[catDict[elt]] += 1
sys.stdout.write("\nCounts for Each Value of Categorical Label \n")
print(list(unique))
print(catCount)
