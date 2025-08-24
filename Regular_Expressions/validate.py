import re
email = input("What's your email? ").strip()
# ^ means start of the string and $ means end of the string   
# \d means decimal digit
# \D means not a decimal digit
# \s means whitespace characters
# \w word character as well as numbers and underscore
# \W means not word character
# | means or
pattern = r"^(\w|\.)+@(\w+\.)?\w+\.(com|za|edu|org|net|gov)$"
if re.search(pattern, email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
