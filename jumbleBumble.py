#JumbleBumble cryptography
#Writeup by jrke(Dumbledore's Army)

from gmpy2 import iroot

#Reading file
inputs = open("C:\\Users\\user\\Downloads\\JumbleBumble.txt").readlines()

#4 lines per encoded - n, e, c, new line
for i in range(len(inputs)//4):
    n = int(inputs[i*4 + 0])#modulo
    e = int(inputs[i*4 + 1])#public key(exponent)
    c = int(inputs[i*4 + 2])#ciphertext

    #LOGIC - e is small enough(4), so expecting m^e < n so m^e will be = m^e % n, so m will be direct eth root of c
    decoded = bytes.fromhex(hex(iroot(c, e)[0])[2:]).decode()

    if "VishwaCTF{" in decoded:
        print(f"Flag = {decoded}")
        break
#flag - VishwaCTF{c4yp70gr2phy_1s_n07_e25y}