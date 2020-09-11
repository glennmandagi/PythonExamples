# call scipy package
import numpy as np
from scipy import stats

# input data
x = [77, 50, 99, 60, 90, 82, 93, 75, 86, 99, 55, 79]

# numpy.std method
get_population_std = np.std(x, ddof=1)
get_population_mean = np.sum(x) / (len(x))

# output
print("Input x : ", x)
print("Population Standard Deviation of x : {0}".format(get_population_std))
