def is_binary(num):
    while num!=0:
        l=num%10
        if l!=0 and l!=1:
            return False
        num=num//10
    return True





print(is_binary(11000111))