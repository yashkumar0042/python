import numpy as np

# 0-D array (scalar)
scalar = np.array(42)
print("Scalar (0-D) array:", scalar)
print("Number of dimensions:", scalar.ndim)
print("Shape:", scalar.shape)
print()

# 1-D array (vector)
arr_1d = np.array([1, 2, 3, 4, 5])
print("1-D array:", arr_1d)
print("Number of dimensions:", arr_1d.ndim)
print("Shape:", arr_1d.shape)
print()

# 2-D array (matrix)
arr_2d = np.array([[1, 2, 3], 
                   [4, 5, 6]])
print("2-D array:\n", arr_2d)
print("Number of dimensions:", arr_2d.ndim)
print("Shape:", arr_2d.shape)
print()

# 3-D array
arr_3d = np.array([[[1, 2, 3], 
                     [4, 5, 6]],

                    [[7, 8, 9], 
                     [10, 11, 12]]])
print("3-D array:\n", arr_3d)
print("Number of dimensions:", arr_3d.ndim)
print("Shape:", arr_3d.shape)
