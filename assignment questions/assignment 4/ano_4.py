#wap to create a function the prints the first 15 terms of the fibonacci series without using recursion.
def fibonacci(n):
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
n=int(input("Enter the no.of terms you want to print :"))
print("The fibonacci series of first ",n,"terms are:")
fibonacci(n)