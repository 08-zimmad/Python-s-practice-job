
# using strings
def isPalindrome(x: int) -> bool: # returns Bool value
    str_num=str(x) 
    str_num=str_num[::-1] # this slicing is used for reversing the list/string
    return str(x)==str_num




# using Loop
def isPalindrome2(x: int) -> bool:
    if x<0:
        return False
    num=x   
    reverse=0   # for storing the reversed integer
    while num!=0:
        digit=num%10  # eg 121 ,, the % would give the reminder which is 1
        reverse=reverse*10+digit # initialy: 0=0*10+1 -> 1
        num=num//10 # 121//10=12
    return reverse==x


print(isPalindrome2(-121))