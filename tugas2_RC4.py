def KSA (key):
    key_length = len (key)
    s = list(range(256))
    j = 0
    for i in range (256):
        j = (j + s[i] + key [i%key_length])%256
        s[i],s[j] = s[j],s[i]

    return s

def PRGA (s,n):
    i = 0
    j = 0
    key = []

    while n>0:
        n = n-1
        i = (i + 1) % 256
        j = (j +s[i]) % 256
        s[i],s[j] = s[j],s[i]
        k = s[(s[i] + s[j]) % 256]
        key.append(k)
    return key

key = input("masukkan key = ")
plainteks = input("masukkan plainteks = ")

def preparing_key_array(s):
    return [ord(c) for c in s]

key = preparing_key_array(key)

import numpy as np
s = KSA(key)

keystream = np.array(PRGA(s, len(plainteks)))
print(keystream)

plainteks = np.array([ord(i) for i in plainteks])

cipher = keystream ^ plainteks

print(cipher.astype(np.uint8).data.hex())
print([chr(c) for c in cipher])

