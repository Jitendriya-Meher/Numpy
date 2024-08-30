# NumPy Arrays
# 1. Performance:

# Speed: NumPy arrays are implemented in C and Fortran, which allows for much faster computations compared to Python lists. Vectorized operations are optimized for performance.
# Memory Efficiency: NumPy arrays are more memory-efficient because they use contiguous blocks of memory and have fixed-size data types.
# 2. Data Types:

# Homogeneity: All elements in a NumPy array must be of the same type, which ensures that operations can be performed efficiently.
# Data Type Specification: You can specify the data type of the array elements, which can help in optimizing memory usage.
# 3. Operations:

# Vectorization: NumPy supports element-wise operations and broadcasting, allowing you to perform operations on entire arrays without explicit loops.
# Mathematical Functions: NumPy provides a rich set of mathematical functions, including trigonometric, statistical, and linear algebra operations.
# 4. Indexing and Slicing:

# Advanced Indexing: NumPy supports advanced indexing and slicing, including boolean indexing and fancy indexing.
# Broadcasting: Operations on arrays of different shapes are handled automatically through broadcasting.
# 5. Shape and Reshaping:

# Multi-Dimensional Arrays: NumPy supports multi-dimensional arrays (e.g., 2D matrices, 3D tensors) and provides functions to reshape and manipulate these arrays.
# 6. Interoperability:

# Integration: NumPy arrays integrate well with other libraries like Pandas, SciPy, and Matplotlib, making them a central component of the scientific Python ecosystem.


# Python Lists
# 1. Performance:

# Speed: Python lists are slower for numerical computations because they are implemented in pure Python and involve more overhead.
# Memory Usage: Python lists are less memory-efficient since they can store mixed data types and require additional memory for type information and pointers.
# 2. Data Types:

# Heterogeneity: Python lists can store elements of different types (e.g., integers, strings, objects), which provides flexibility but can be less efficient for numerical tasks.
# 3. Operations:

# Element-wise Operations: Python lists do not support element-wise operations out of the box. You need to use loops or list comprehensions for such operations.
# Limited Mathematical Functions: Python lists do not provide built-in mathematical functions; you need to use additional libraries or write custom functions.
# 4. Indexing and Slicing:

# Basic Indexing: Python lists support basic indexing and slicing but do not support advanced indexing or broadcasting.
# 5. Shape and Reshaping:

# Single-Dimensional: Python lists are inherently one-dimensional, though you can create nested lists to simulate multi-dimensional structures. Reshaping requires manual manipulation.
# 6. Interoperability:

# Less Integration: While Python lists are versatile, they are not as seamlessly integrated with scientific libraries as NumPy arrays.


from datetime import datetime
import numpy as np

# Record start time
start_time = datetime.now()

[j**4 for j in range(1,900000)]

# Record end time
end_time = datetime.now()

# Calculate elapsed time
elapsed_time = end_time - start_time
print("time = ",elapsed_time)


# Record start time
start_time = datetime.now()

np.arange(1,900000)

# Record end time
end_time = datetime.now()

# Calculate elapsed time
elapsed_time = end_time - start_time
print("time = ",elapsed_time)