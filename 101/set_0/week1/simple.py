def LetterChanges(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    s.lower()
    for ch in s:
        if ch.isalpha():
            tmp = ord(ch) + 1
            if tmp <= ord('z'):
                if chr(tmp) in vowels:
                    res.append(chr(tmp).upper())
                else:
                    res.append(chr(tmp))
            else:
                res.append('a'.upper())
        else:
            res.append(ch)
    res = "".join(res)
    print(res)

LetterChanges("helzlo*3z")
