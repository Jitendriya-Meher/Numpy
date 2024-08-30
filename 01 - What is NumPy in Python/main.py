# NumPy (short for Numerical Python) is a fundamental Python library used for numerical computing. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays. NumPy is widely used in data science, machine learning, scientific computing, and engineering because of its powerful capabilities and performance.

# Advantages of NumPy:
# Performance:

# Fast Computations: NumPy operations are implemented in C and Fortran, providing high performance and speed for numerical computations compared to pure Python code.
# Vectorization: NumPy allows for vectorized operations, meaning computations are applied to entire arrays at once, reducing the need for explicit loops and speeding up operations.
# Memory Efficiency:

# Compact Data Storage: NumPy arrays use less memory than Python lists because they store data in a contiguous block of memory and are typed arrays.
# Data Type Specification: NumPy arrays have a fixed data type, which allows for more efficient memory usage.
# Rich Functionality:

# Mathematical Functions: NumPy provides a wide range of mathematical functions for operations such as trigonometry, linear algebra, statistics, and more.
# Array Manipulation: Functions for reshaping, slicing, and indexing arrays are available, making data manipulation flexible and efficient.
# Interoperability:

# Integration with Other Libraries: NumPy arrays are compatible with other Python libraries like Pandas, Matplotlib, SciPy, and TensorFlow, facilitating a seamless workflow in data science and machine learning.
# Broadcasting:

# Flexible Operations: Broadcasting allows NumPy to perform operations on arrays of different shapes, automatically aligning them for element-wise operations.
# Community and Support:

# Well-Established: NumPy is a well-established library with extensive documentation and a large user community, making it easier to find support and resources.
# Disadvantages of NumPy:
# Limited Data Types:

# Homogeneous Arrays: NumPy arrays are homogeneous, meaning all elements must be of the same type. This can be restrictive when dealing with heterogeneous data or mixed data types.
# Learning Curve:

# Complex Syntax: For beginners, the syntax and concepts of NumPy, such as broadcasting and advanced indexing, can be challenging to master initially.
# No Built-in DataFrame:

# Data Structures: Unlike Pandas, NumPy does not provide built-in support for DataFrames, which are useful for working with tabular data. Users often need to integrate NumPy with Pandas for this functionality.
# Not Suitable for All Applications:

# Specialized Tasks: NumPy is optimized for numerical computations and may not be suitable for all types of applications, such as symbolic mathematics or certain types of data processing.
# Overhead with Small Arrays:

# Memory Overhead: For very small arrays, the overhead of using NumPy might not be justified compared to simple Python lists or arrays.
# Global Interpreter Lock (GIL):

# Concurrency: NumPy’s performance can be limited by Python’s Global Interpreter Lock (GIL) when performing multi-threaded operations, though this is often mitigated by NumPy's use of C extensions.

import numpy as np

print("numpy : ",np)

x = [1,2,3,4]

print(x)
print(type(x))

xs = np.array([1,2,3,4])

print(xs)
print(type(xs))