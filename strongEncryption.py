#StrongEncryption web
#Writeup by jrke(Dumbledore's Army)

#A simple php + crypto chall
#I just ran given php code with some more echo commads which gave me key and hash of key and the key hex which has to be removed from the encrypted text
#key hex came - 45
#hash of key - 2f12f4712f4c769a75b33cb995fa169056168939a8b0b28eafe0d724f18dc4a7
#removing it from encrypted text gave 576e78697e65445c4a7c8033766770357c3960377460357360703a6f6982
#key came to be - 155174184173188166136153139
key = "155174184173188166136153139"
enc = "576e78697e65445c4a7c8033766770357c3960377460357360703a6f6982"
flag = ""

#Brute forcing letter wise letter
for i in range(len(enc)//2):#//2 because enc is in hex
    for k in range(200):
        if hex((int(key[i%len(key)]) + k))[2:] == enc[i*2:i*2 + 2]:
            flag += chr(k)
            break

print(f"{flag = }")
#flag - VishwaCTF{y0u_h4v3_4n_0p_m1nd}