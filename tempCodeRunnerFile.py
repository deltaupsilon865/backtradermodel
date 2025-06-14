import numpy as np 
a=np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)  #get rows and columns
print(a[1,2])   #get element at row 1 and column 2
print(a[0,:])   #get row 0
print(a[:,1])   #get column 1
print(a[0,1:3]) #get row 0 and column 1 to 3
print(np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])) #3D array