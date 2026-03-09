#wap to print the second larjest and smallest element in a list of 10 integers without using sort function.
arr=[]
x = int(input("enter the no.of elements :"))
for i in range(x):
    m = int(input("enter the element :"))
    arr.append(m)
for j in range(len(arr)-1):
    for k in range(len(arr)-j-1):
        if arr[k]>arr[k+1]:
            arr[k],arr[k+1]=arr[k+1],arr[k]
print("The stored array is :")
print(arr)
second_largest=arr[-2]
second_smallest=arr[1]
print("Second largest element is :",second_largest)
print("Second smallest element is :",second_smallest)