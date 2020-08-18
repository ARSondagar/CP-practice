# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import stats
size = int(input())
arr = np.array([int(i) for i in input().split()])
print(np.mean(arr))
print(np.median(arr))
print(int(stats.mode(arr)[0]))
