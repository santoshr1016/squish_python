import re

# string = 'hello 12 hi 89. Howdy 34 sant1.'
# pattern = '\d+'

# result = re.findall(pattern, string)
# print(result)
# result = re.split(pattern, string)
# print(result)
# result = re.split(pattern, string, 1)  # split only at the first occurrence
# print(result)
string = 'abc 12\
de 23 \n f45 6'
# matches all whitespace characters
pattern = '\s+'
# empty string
replace = ''

# new_string = re.sub(pattern, replace, string)
# print(new_string)

new_string = re.sub(r'\s+', replace, string, 1)
print(new_string)