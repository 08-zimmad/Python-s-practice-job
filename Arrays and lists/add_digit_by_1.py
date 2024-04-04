# given a list of integers represeting a large number 123->[1,2,3]
# add 1 to it and return a list of o/p 123+1=124-> [1,2,3+1]->[1,2,4]
from typing import List

def plusOne(digits: List[int]) -> List[int]:
    for i in range(len(digits)-1,-1,-1):  # 2nd -1 is for reversing, 3rd -1 is for decrement by -1
        if digits[i]==9:
           digits[i]=0
        else:
            digits[i]=digits[i]+1
            return digits
    return [1]+digits



print(plusOne([1,2,3]))
