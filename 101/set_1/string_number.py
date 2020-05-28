'''
1a2s3d4f5g6h7j
'''
import re

def NumberAddition(str):
    total = 0
    res = re.findall(r'\d+', str)
    for item in res:
        total += int(item)
    return total

# keep this function call here
print(NumberAddition(input()))