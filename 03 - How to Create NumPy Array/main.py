import numpy as np

arr = [1,2,3,4,5,6,7,8,9,10]

y = np.array(arr)

print("np array :",y)
print("type :",type(y))

# l = []
# for i in range(1,5):
#     ip = int(input("enter a value : "))
#     l.append(ip)

# y2 = np.array(l)
# print("input array :",y2)

arr2 = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]

print(arr2)
y3 = np.array(arr2)
print(y3)

print("dimension : ",y3.ndim)

y4 = np.array([1,2,3,4], ndmin=10)
print(y4)
print("dimension : ",y4.ndim)