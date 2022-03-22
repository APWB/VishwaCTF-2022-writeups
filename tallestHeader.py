#TallestHeader cryptography
#Writeup by jrke(Dumbledore's Army)

#on opening file in notepad it was looking files are there so i applied binwalk and got script.py and info.txt
#It looks like its shuffling the character's index
#so i just made a dummy string and encrypted it
#compared it with the original and with similarity i decoded the flag

key = [2,1,3,5,4]
ciphertext = "RT1KC _YH43 3DRW_ T1HP_ R3M7U TA1N0"
dummy = "abcdefghijklmnopqrstuvwxyz1234567890"[:len(ciphertext)-ciphertext.count(" ")]


def encrypt(key, plaintext):
    plaintext = "".join(plaintext.split(" ")).upper()
    ciphertext = ""
    for pad in range(0, len(plaintext) % len(key) * -1 % len(key)):
        plaintext += "X"
    for offset in range(0, len(plaintext), len(key)):
        for element in [a - 1 for a in key]:
            ciphertext += plaintext[offset + element]
        ciphertext += " "
    return ciphertext[:-1]

encryptedDummy = encrypt(key, dummy).lower()
flag = "vishwaCTF{"
for e in dummy:#similarity is there so comparing
    flag += ciphertext[encryptedDummy.index(e)].lower()
flag += "}"

print(f"{flag = }")
#flag - vishwaCTF{tr1cky_h34d3r_w1th_p3rmu7at10n}
