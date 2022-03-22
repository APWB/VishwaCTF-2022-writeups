#BetGame reversing
#Writeup by jrke(Dumbledore's Army)

#Winning bet with randomness is quite annoying
#For solving sage.py input i brute forced letter wise here is the script

sage_words = "ǏǇǣŻǏƟƣƷƫƣƷƛŻƷƓƛƓǏƣǗƓƯǣ"

def _0000xf69(passed_strr):
    _0000xf42=''
    for _0000xf72 in passed_strr:
        _0000xf96 = _0000xf106(_0000xf72)
        _0000xf42 = _0000xf42+chr(2*(ord(_0000xf96))+1)
        
        
    return _0000xf42

def _0000xf106(passed_char):
    return chr(2*(ord(passed_char))-1)

hint = ""
for i in sage_words:
    for k in range(1, 2**8):
        if _0000xf69(chr(k)) == i:
            hint += chr(k)
            break

print(f"{hint = }")

#hint = 'try_thinking_negetively'
#with this i discovered i can send a big negative value as bet amount and then losing the bet will give me money
#by which i can buy the flag
#Flag - vishwaCTF{$tr!k3_!t_lu<ky}