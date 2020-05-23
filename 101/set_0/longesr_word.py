from collections import defaultdict
def LongestWord(sen):
    nw = ""
    for letter in sen:
        if letter.isalpha() or letter.isspace() or letter.isnumeric():
            nw += letter
    print(nw)
    return max(nw.split(), key=len)

# print(LongestWord(input()))


def AlphabetSoup(s):
  s = sorted(s)
  return "".join(s)

# keep this function call here
print(AlphabetSoup(input()))