nums = [0 for i in range(10)]
print(nums)


# divisible of 3 in lists using comprehension
divisible_of_3=[i for i in range(10) if i % 3 == 0]
print(divisible_of_3)


# making uppercase using comprehension
s = 'Bye'
l = [char.upper() for char in s]
print(l)


# list of factorial using comprehension
def factorial(n):
    if n==0:
        return 0
    fact=1
    for i in range(1,n+1):
        fact=fact * i
    return fact

get_fact_upto_10=[factorial(i) for i in range(10)]
print(get_fact_upto_10)



# fibonacci using comprehension
n=int(input())
mylist=[0,1]
[mylist.append(mylist[-2]+mylist[-1]) for i in range(n)]
print(mylist)