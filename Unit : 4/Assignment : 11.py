#Assignment : 11
import pandas as pd
import numpy as np

# creating series with ten random numbers
nums = pd.Series(np.random.randint(1, 100, 10))

print("Series created")
print(nums)

# indexing
print("First value is", nums[0])
print("Last value is", nums[9])
print("First three values are")
print(nums[0:3])

# filtering
print("Values greater than 50 are")
print(nums[nums > 50])

# statistical operations
print("Mean is", nums.mean())
print("Median is", nums.median())
print("Minimum is", nums.min())
print("Maximum is", nums.max())

#Output
'''Series created
0    39
1    30
2    73
3    19
4    58
5    62
6    93
7    95
8    74
9    33
dtype: int64
First value is 39
Last value is 33
First three values are
0    39
1    30
2    73
dtype: int64
Values greater than 50 are
2    73
4    58
5    62
6    93
7    95
8    74
dtype: int64
Mean is 57.6
Median is 60.0
Minimum is 19
Maximum is 95'''