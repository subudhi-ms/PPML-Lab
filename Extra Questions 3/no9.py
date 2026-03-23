import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])
arr2 = np.array([[9,10], [11,12], [13,14], [15,16]])
x1, y1 = arr.shape
x2, y2 = arr2.shape
arr3 = np.zeros((x1, y2))
print(x1,y1,x2,y2)

if y1 == x2:
    for i in range(x1):
        for j in range(y2):
            for k in range(y1):
                arr3[i][j] += (arr[i][k] * arr2[k][j])

    print("After matrix multiplication :\n", arr3)
else:
    print("Array multiplication is not possible.")
