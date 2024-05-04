
import string


print("Alphabet from a-z:")
for letter in string.ascii_lowercase:

    print(letter, ord(letter), end=" ")
    


print()

# 95 - 90 A-Z
# 97 - 122 a-z
print("Alphabet from A-Z:")
for letter in string.ascii_uppercase:
    print(letter,ord(letter), end=" ")