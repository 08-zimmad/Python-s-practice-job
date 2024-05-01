import re


# Searches for the first occurrence of a pattern in a string.
match = re.search(r'is', 'This is a string')
if match:  # Object type match or None
    print("Pattern found:", match.group())



# Matches a pattern only at the beginning of the string.
match = re.match(r'This', 'This is a string')
if match: # Object type match or None
    print("Pattern found:", match.group())



# returns list of all occurrences
matches = re.findall(r'is', 'This is a istring')
print("findall",matches)



#Finds all occurrences of a pattern in a string.
matches = re.finditer(r'is', 'This is a string')   #
for match in matches:  #Iterator of Match objects
    print("finditer:", match.group())


# Substitutes occurrences of a pattern in a string with another string.
new_string = re.sub(r' is', ' was', 'This is a string')
print("sub",new_string)



# Compiles a regular expression pattern into a regex object.
# This object has methods like search(), match(), findall(), etc.
pattern = re.compile(r'is')
match = pattern.findall('This is a string') #Return Type: Pattern object
if match:
    print("Pattern found:", match)



# Splits a string by occurrences of a pattern.
parts = re.split(r'\s+', 'This is a string') # splits whole array into list of words
print("split",parts)