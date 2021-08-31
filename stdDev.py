import pandas as pd
import math

df = [60,61,65,63,98,99,90,95,91,96]




total = 0
total_sum = 0
total_entries = len(df)

for total in df:
    total_sum += float(total)

mean = total_sum / total_entries
print("Mean (Average) is -> "+str(mean))


sumOfSquares = 0

for i in df:
    a = float (i)- mean
    b = a*a 
    sumOfSquares= sumOfSquares + b 

result = sumOfSquares/(total_entries-1)

std = math.sqrt(result)

print ("Sum of squares is ->", sumOfSquares)
print("this is the variance", result)
print("the standard deviation is", std)

import statistics

std1 = statistics.stdev(df)

print("Statistics =", std1)
