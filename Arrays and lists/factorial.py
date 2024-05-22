def fac(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    print("factorial:", res)




# using recursion

def fac1(n):
    if n==0 or n==1:
        return 1
    return n * fac1(n-1)

print(fac1(5))