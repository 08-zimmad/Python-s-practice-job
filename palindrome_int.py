
# using strings
def isPalindrome(x: int) -> bool:
    str_num=str(x)
    str_num=str_num[::-1]
    return str(x)==str_num




# using Loop
def isPalindrome2(x: int) -> bool:
    if x<0:
        return False
    num=x
    reverse=0
    while num!=0:
        digit=num%10
        reverse=reverse*10+digit
        num=num//10
    if x==reverse:
        return True
    return False


print(isPalindrome2(-121))