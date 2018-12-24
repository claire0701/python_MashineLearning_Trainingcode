# python_MashineLearning_Trainingcode

This code is only used for my study of machine learing in python --> only for fun!

Today, we will have a look at this dataset on “Sonar: Mines vs. Rocks” by Gorman and Sejnowski.

This dataset dates back to the Cold War and consists of sonar data. The name and setup suggests that the aim of this data is do distinguish between rocks and metal structures such as sea mines on the seafloor. The experimental setup was as follows:

a metal cylinder and a cylindrical rock, both of length 5 ft, placed on sandy ocean floor
sonar impulse: wide-band linear FM
return sampling in a distance of 10 meters
return sample aspect angle: spanning 90° (metal cylinder) and 180° (rock)
input data is a normalized spectral envelope covering 60 samples (hence it is heavily pre-processed already and is not a time series but the result of one)
208 samples selected from 1200 (by which criteria?); 111 metal samples, 97 rock samples