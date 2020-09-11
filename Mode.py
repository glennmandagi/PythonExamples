# call scipy package
from scipy import stats

# input data
x = [77, 50, 99, 60, 90, 82, 93, 75, 86, 99, 55, 79]

# stats.mode methods
get_mode = stats.mode(x)

# output
print("Input x : ", x)
print("Median of x : ", get_mode[0])
