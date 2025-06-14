import numpy as np 
# a=np.array([[1,2,3],[4,5,6]])
# print(a)
# print(a.shape)  #get rows and columns
# print(a[1,2])   #get element at row 1 and column 2
# print(a[0,:])   #get row 0
# print(a[:,1])   #get column 1
# print(a[0,1:3]) #get row 0 and column 1 to 3
# b=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])) #3D array
# print(b.shape) #get rows and columns
# print(b.diagonal) #get number of dimensions
# print(b[:,1,1]) #get row 1 and column 1
# print(b[0,1,1]) #get row 0 and column 1
# print(np.full((2,3,3),8))   #create 3D array with all elements as 8
# print(np.random.randint(8, size=(3,3))) #create 3D array with random elements
# arr=np.array([[1,2,3],[4,5,6]])
# r1=np.repeat(arr,3,axis=0) #repeat array 3 times along row
# print(r1)
# output=np.ones((6,6)) #create 2D array with all elements as 1
# z=np.zeros((4,4)) #create 2D array with all elements as 0
# z[1:3,1:3]=2 #set element at row 1,2 and column 1,2 as 2
# output[1:5,1:5]=z
# print(output)
a=np.array([[1,2,3],[4,5,6]])
b=a.copy() #copy array
b[0,0]=99 #set element at row 0 and column 0 as 99
print(a) #original array
print(b) #copied array