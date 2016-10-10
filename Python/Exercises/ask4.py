import math



a=input("Dose ton ari8mo a:")
a=float(a)
print(a)

b=input("Dose ton ari8mo b:")
b=float(b)
print(b)

c=input("Dose ton ari8mo c:")
c=float(c)
print(c)

if (b**2)-4*a*c>0:
    
        r=float(b**2-4*a*c)

        print("H diakrinousa einai: ",r)
        
        X1=(-b+math.sqrt(r))/2*a

        X2=(b+math.sqrt(r))/2*a
    
        print("H deuteroba8mia eksiswsh exei X1=  ",X1)
        print("H deuteroba8mia eksiswsh exei X2=  ",X2)

else:

        print("There is no real-valued solutios")
        

