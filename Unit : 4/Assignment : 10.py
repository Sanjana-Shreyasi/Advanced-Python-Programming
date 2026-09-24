#Assignment : 10
import numpy as np

nums = np.arange(1, 11)

print("Array created")
print(nums)

first_five = nums[0:5]
last_five = nums[5:10]

print("First five values are")
print(first_five)

print("Last five values are")
print(last_five)

print("Sum of array is", nums.sum())
print("Mean of array is", nums.mean())
print("Maximum value is", nums.max())
print("Minimum value is", nums.min())

new_nums = nums * 2

print("Array after multiplying every value by 2")
print(new_nums)

#Output
'''Array created
[ 1  2  3  4  5  6  7  8  9 10]
First five values are
[1 2 3 4 5]
Last five values are
[ 6  7  8  9 10]
Sum of array is 55
Mean of array is 5.5
Maximum value is 10
Minimum value is 1
Array after multiplying every value by 2
[ 2  4  6  8 10 12 14 16 18 20]'''