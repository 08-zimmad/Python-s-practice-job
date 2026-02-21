# sum of divisors if equal to the given number then its perfect number

def Chk_Perfect(n):
    sum=0
    for i in range (1,((n//2)+1)):
        rem=n%i
        if rem==0:
            sum=sum+i
    if sum==n:
        print("it is a perfect square")
    else:
        print("It is not a perfect square")
 
Chk_Perfect(8)
