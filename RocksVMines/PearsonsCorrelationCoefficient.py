__author__ = 'JHou'

import pandas as pd
from pandas import DataFrame
from math import sqrt
import matplotlib.pyplot as plot
import sys

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

#calculate correlations between real-valued attribute
dataRows2 = rocksVMines.iloc[1, 0:60]
dataRows3 = rocksVMines.iloc[2, 0:60]
dataRows21 = rocksVMines.iloc[20, 0:60]

mean2 = 0.0; mean3 = 0.0; mean21 = 0.0
numElt = len(dataRows2)
for i in range(numElt):
    mean2 += dataRows2[i]/numElt
    mean3 += dataRows3[i]/numElt
    mean21 += dataRows21[i]/numElt


var2 = 0.0; var3 = 0.0; var21 = 0.0
for i in range(numElt):
    var2 += (dataRows2[i] - mean2) * (dataRows2[i] - mean2)/numElt
    var3 += (dataRows3[i] - mean3) * (dataRows3[i] - mean3)/numElt
    var21 += (dataRows21[i] - mean21) * (dataRows21[i] - mean21)/numElt

corr23 = 0.0; corr221 = 0.0
for i in range(numElt):
    corr23 += (dataRows2[i] - mean2) * (dataRows3[i] - mean3) / (sqrt(var2*var3)*numElt)
    corr221 += (dataRows2[i] - mean2) * (dataRows21[i] - mean21) / (sqrt(var2*var21)*numElt)

sys.stdout.write("Correlation between attribue 2 and 3 \n")
print(corr23)
sys.stdout.write(" \n")

sys.stdout.write("Correlation between attribue 2 and 321 \n")
print(corr221)
sys.stdout.write(" \n")

#calculate correlations between real-values atrributes
corMat = DataFrame(rocksVMines.corr())

#visualize correlations using heatmap
plot.pcolor(corMat)
plot.show()