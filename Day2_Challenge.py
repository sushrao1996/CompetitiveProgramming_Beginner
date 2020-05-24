def pattern(n):
    for i in range(1,n+1):
        if i%2!=0:
            k=i+1
        else:
            k=i
        for j in range(k,n):
            print(end=" ")
        for g in range(k):
            print("*",end=" ")
        print("\n")


n=int(input("Enter the number of rows: "))
pattern(n)
    
            
