def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:])+s[0]


s=input("enter a string :")
print("its reverse is : ",reverse(s))
