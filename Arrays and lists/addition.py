def addition(x,y):
    while y!=0:
        carry=x&y
        x=x^y
        y=carry<<1
    return x


a=2
b=23
print(addition(a,b))