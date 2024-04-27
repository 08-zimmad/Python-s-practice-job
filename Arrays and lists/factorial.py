def fac(n):
    res=1
    for i in range(n,0,-1):
        res=res*i
    print("factorial:", res)




# using recursion

def fac1(n):
    rem=1
    if n>0:
        return rem * fac1(n-1)
    return 1
    
print(fac1(5))