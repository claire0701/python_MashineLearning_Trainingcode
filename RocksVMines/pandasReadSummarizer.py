__autor__ = 'Jie Hou'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
from random import uniform

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

#print summary of data frame
summary = rocksVMines.describe()
print(summary)

for i in range(208):
    if rocksVMines.iat[i, 60] == "M":
        pcolor = "red"
    else:
        pcolor = "blue"
    #plot rows of data as if they were series data 
    dataRow = rocksVMines.iloc[i, 0:60]
    dataRow.plot(color=pcolor)

plot.xlabel("Attribue Index")
plot.ylabel(("Attribue Values"))
plot.show()

dataRow2 = rocksVMines.iloc[1, 0:60]
dataRow3 = rocksVMines.iloc[2, 0:60]
plot.scatter(dataRow2, dataRow3)

plot.xlabel("2nd Attribute")
plot.ylabel(("3rd Attribute"))
plot.show()

dataRow21 = rocksVMines.iloc[20, 0:60]
plot.scatter(dataRow2, dataRow21)
plot.xlabel("2nd Attribute")
plot.ylabel(("21rd Attribute"))
plot.show()

#change the targets to numeric values
target = []
for i in range(208):
    if rocksVMines.iat[i, 60] == "M":
        target.append(1.0)
    else:
        target.append(0.0)
dataRow = rocksVMines.iloc[0:208, 35]
plot.scatter(dataRow, target)

plot.xlabel("Attribure Value")
plot.ylabel("Target Value")
plot.show()

#To improve the visualization, this version dithers the points a litte
# and make them somewhat transparent
target = []
for i in range(208):
    #assign 0 or 1 target value based on "M" or "R" labels
    # adn add some dither
    if rocksVMines.iat[i, 60] == "M":
        target.append(1.0 + uniform(-0.1, 0.1))
    else:
        target.append(0.0 + uniform(-0.1, 0.1))
dataRow = rocksVMines.iloc[0:208, 35]
plot.scatter(dataRow, target, alpha=0.5, s=120)
plot.xlabel("Attribure Value")
plot.ylabel("Target Value")
plot.show()
