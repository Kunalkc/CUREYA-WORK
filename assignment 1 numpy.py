#using numpy
# NAME- KUNAL CHANDEL
import numpy
from scipy import stats

givenval = (3,4,5,6,1,2,45,32,56,56,89,90,12,54,45,9,67,68,31,32)
mean = numpy.mean(givenval)
print("mean is", mean)

median = numpy.median(givenval)
print("median is", median)

mode = stats.mode(givenval)
print("mode is", mode)