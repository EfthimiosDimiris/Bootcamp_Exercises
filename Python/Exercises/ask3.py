import math



a=input("Give side a:")
a=float(a)
print(a)

b=input("Give side b:")
b=float(b)
print(b)

c=input("Give side c:")
c=float(c)
print(c)


r=((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))

A=(1/4)*(math.sqrt(r))

print("The result is ",A)

