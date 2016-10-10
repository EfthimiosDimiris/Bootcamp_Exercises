for sum in range(1):
    sum=input("\nEnter number of pronic numbers: ")
    sum=int(sum)

    for n in range(1,sum):
        
        Pronic_number= int(n*(n+1))
            
        print(Pronic_number,end=",")
