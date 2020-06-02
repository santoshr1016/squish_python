def BinaryReversal(str):
    binary = list(bin(int(str))[2:])
    len_binary = len(binary)
    if len_binary <= 8:
        binary = ['0']*(8-len_binary) + binary
    elif 8 < len_binary <= 16:
        binary = ['0'] * (16 - len_binary) + binary
    binary.reverse()
    binary = ''.join(binary)
    binary = '0b' + binary
    return int(binary, 2)

# keep this function call here
print(BinaryReversal(input()))