import numpy as np

# zero 
arr_zero = np.zeros(4)
print("zeroes arra :",arr_zero)

arr_zero2 = np.zeros((3,2,2))
print("zeroes arra :",arr_zero2)

# ones 
arr_one = np.ones(4)
print("zeroes arra :",arr_one)

arr_one2 = np.ones((3,2,2))
print("zeroes arra :",arr_one2)

#empty
arr_em = np.empty(3)
print("empty array :",arr_em)

#range
arr_ng = np.arange(10)
print("range array :",arr_ng)

#diagonal elements 1
arr_dia = np.eye(3,4)
print("diagonal element 1 :",arr_dia)

# line space
arr_li = np.linspace(0,10,num=5)
print("line space array :",arr_li)