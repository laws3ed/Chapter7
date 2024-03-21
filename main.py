from chapter7.pycode import convertToList
import numpy as np

# create numpy array
arr = np.array([1, 2, 4, 5])
print("Before conversion: ", arr)
print(type(arr))
# Convert numpy array to list
arr_list = convertToList(arr)
print("\nAfter conversion: ", type(arr_list))
print(arr_list)
