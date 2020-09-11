# call numpy package
import numpy as np

# input data
x = [77, 50, 99, 60, 90, 82, 93, 75, 86, 99, 55, 79]

# numpy.std method
get_sample_std = np.std(x, ddof=1)
get_sample_mean = np.sum(x) / (len(x) - 1)

# output
print("Input x : ", x)
print("Sample Standard Deviation of x : ", get_sample_std)
