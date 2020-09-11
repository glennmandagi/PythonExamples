# call scipy package
import numpy as np
from scipy import stats

# input data
x = [77, 50, 99, 60, 90, 82, 93, 75, 86, 99, 55, 79]

# numpy.std method
get_sample_std = np.std(x, ddof=1)
get_population_mean = np.sum(x) / (len(x))

# calculate coefficient of variation
get_cv = (get_sample_std * 100) / get_population_mean

# output
print("Sample of mean of x : ", get_population_mean)
print("Coeefficient of variation: {0}".format(get_cv))
