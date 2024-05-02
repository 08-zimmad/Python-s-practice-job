def addition(x,y):
    while y!=0:
        carry=x&y
        x=x^y
        y=carry<<1
    return x


a=21
b=2
print(addition(a,b))