#call numpy package
import numpy as np

#input data
x = [77, 50, 99, 60, 90, 82, 93, 75, 86, 99, 55, 79]

#numpy.mean(), sum(), and len()
get_sample_mean = np.sum(x) / (len(x) - 1)

print("Input : ", x)
print("Sample mean of x : ", get_sample_mean)
