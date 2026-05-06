import re
email = input("what's your email? ")
pattern = re.search("/.", email)
print(pattern.span())









