import numpy as np

#python LIST
py_list=[1,2,3,4,5,6,7,8,9]

#numpy ARRAY
np_array=np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))
print(type(np_array))

py_multi=[[1,2,3],[4,5,6],[7,8,9]]
np_multi=np_array.reshape(3,3) #it is a matrix

print(py_multi)
print(np_multi)

print(np_array.ndim)
print(np_multi.ndim)

print(np_array.shape) # 1 dimension
print(np_multi.shape) # 3*3 dimension
