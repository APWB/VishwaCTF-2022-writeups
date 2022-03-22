#RunTheCat reversing
#Writeup by jrke(Dumbledore's Army)

#I just copy pasted code from the file provided and just removed few lines and edited few
#On analysing i discovered brute forcing is easy if i break the input of lenght 9 into 3 parts each of lenght 3
#So thats what i did for each payload of lenght 3 it finds the nearest match to the final encrypted text and continues the search
#payload1 = string of any 3 digit int
#payload2 = string of any 3 characters
#payload3 = string of any 3 digit int

CAT = int
cAT = len
CaT = print
RAT = str
CATCATCATCATCATCAT = RAT.isdigit

def Kitty(cat):
    return RAT(CAT(cat)*CATCATCAT)

def CAt(cat, cats):
    cat1 = 0
    cat2 = 0
    catcat = 0
    cAt = ""
    while cat1 < cAT(cat) and cat2 < cAT(cats):
        if catcat%CATCATCAT == CATCATCATCATCAT//CATCATCATCAT:
            cAt += cats[cat2]
            cat2 += 1
        else:
            cAt += cat[cat1]
            cat1 += 1
        catcat += 1
    return cAt

def catt(cat):
    return cat[::CATCATCAT-CATCATCATCAT]

def caT(cat):
    return Kitty(cat[:CATCATCAT]) + catt(cat)

def rAT(cat):
    return cat

def Rat(cat):
    return "Cat" + RAT(cAT(cat)) + cat[:CATCATCAT]

def Cat(cat):
    if cAT(cat) == 9:
        if CATCATCATCATCATCAT(cat[:CATCATCAT]) and\
            CATCATCATCATCATCAT(cat[cAT(cat)-CATCATCAT+1:]):
                catcat = CAt(caT(cat), Rat(rAT(catt(cat))))
                return catcat
        else:
            pass
    else:
        pass

f = "000aaa000"
toSearch = "C20a73t0294t0ac2194"

payload1 = "0"
matches = 0
for i in range(100, 1000):
    cat = str(i) + "aaa000"
    cat = cat[:9]
    CATCATCAT = cAT(cat)//3
    CATCATCATCAT = CATCATCAT+1
    CATCATCATCATCAT = CATCATCAT-1
    enc = Cat(cat)
    curr = 0
    for p in range(len(enc)):
        if enc[p] == toSearch[p]:
            curr += 1
    if curr > matches:
        matches = curr
        payload1 = str(i)
print(f"{payload1 = }")

payload2 = "0"
matches = 0
for a in "abcdefghijklmnopqrstuvwxyz":
    for b in "abcdefghijklmnopqrstuvwxyz":
        for c in "abcdefghijklmnopqrstuvwxyz":
            cat = payload1 + a + b + c + "000"
            CATCATCAT = cAT(cat)//3
            CATCATCATCAT = CATCATCAT+1
            CATCATCATCATCAT = CATCATCAT-1
            enc = Cat(cat)
            curr = 0
            for p in range(len(enc)):
                if enc[p] == toSearch[p]:
                    curr += 1
            if curr > matches:
                matches = curr
                payload2 = a + b + c
print(f"{payload2 = }")

payload3 = ""
for i in range(100, 1000):
    cat = payload1 + payload2 + str(i)
    cat = cat[:9]
    CATCATCAT = cAT(cat)//3
    CATCATCATCAT = CATCATCAT+1
    CATCATCATCATCAT = CATCATCAT-1
    enc = Cat(cat)
    if enc == toSearch:
        payload3 = str(i)
        break
print(f"{payload3 = }")

finalPayload = payload1 + payload2 + payload3
flag = "VishwaCTF{runner_" + finalPayload + "}"

print(f"{flag = }")
#flag - VishwaCTF{runner_691cat420}