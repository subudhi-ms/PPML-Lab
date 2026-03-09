#wap to create an integer list of 20 elements increase the odd valued element by 5.
s=[]
x = int(input("enter the no.of elements :"))
for i in range(x):
    n = int(input("enter the element :"))
    s.append(n)
for i in range(x):
    if s[i]%2!=0:
        s[i]+=5
print(s)