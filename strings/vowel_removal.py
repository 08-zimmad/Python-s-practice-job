
str="my name is zimmad"
result=""
for s in str:
    
    if s in ('a','e','i','o','u'):
        s=""
    result+=s
print(result)





# using regex
import re

# str="my name is zimmad"
str=re.sub("[a,e,i,o,u]","",str)
print(str)