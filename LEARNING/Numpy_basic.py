import numpy as np 

print(np.__version__)

a = np.array([0,1,2,3,4])
print(a)
print(type(a))
print(a.dtype)


b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
print(type(b))
print(b.dtype)

a[0]=100
print(a)

a[1]=20
print(a)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr[1:8:2])

print(arr.size)
print(arr.ndim)
print(arr.shape)

mean=arr.mean()
print(mean)

standard_deviation=arr.std()
print(standard_deviation)

print(arr.max())
print(arr.min())


# Numpy Array Addition

u = np.array([1,0])
print(u)

v= np.array([0,1])
print(v)

z = np.add(u,v)
print(z)

y = np.subtract(u,v)
print(y)


arr1 = np.array([1,2])
arr2 = np.array([2,1])

arr3 = np.multiply(arr1,arr2)
print(arr3)

arr4 =np.divide(arr1,arr2)
print(arr4)


#DOT product

X= np.array([3,5])
Y= np.array([2,4])

XY= np.dot(X,Y)
print(XY)


#linspace

lin = np.linspace(5,4,num=6)
print(lin)