# call numpy package
import numpy as np

# input data
x = [77, 50, 99, 60, 90, 82, 93, 75, 86, 99, 55, 79]

# numpy.var method
get_sample_var = np.var(x, ddof=1)

# output
print("Input x : ", x)
print("Sample Variance of x : ", get_sample_var)
