#call numpy package
import numpy as np

#input data
x = [77, 50, 99, 60, 90, 82, 93, 75, 86, 99, 55, 79]

#numpy.mean(), sum() and len() methods
get_population_mean = np.sum(x) / (len(x))

print("Input : ", x)
print("Population mean of x : ", get_population_mean)
