def varAnpassung(i):
    if ord(i) in range(97, 123):
        var = [96, 122, 97]
        
    else:
        var = [64, 90, 65]
    
    return var 


def vigVer(text, key):
    x = 0
    textNew = ""

    for i in text:

        var1, var2, var3 = varAnpassung(i)

        shifts = ord(key[x]) - var3
        numChrOld = ord(i)
        numChrNew = numChrOld + shifts
    
        if numChrNew > 122:
            numChrNew = var1 + numChrNew - var2
        
        textNew = textNew + chr(numChrNew)
    
        # plus zwei da elemente bei 0 und len bei 1 anfangen
        if x+2 > len(key):
            x = 0
        else:
            x +=1
    
    return textNew


def vigEnt(textVer, key):
    x = 0
    klartext = ""

    for i in textVer:

        # var1, var2, var3 = varAnpassung(i)

        shifts = ord(key[x]) - 97
        numChrVer = ord(i)
        numChrEnt = numChrVer - shifts

        if numChrEnt < 97:  
            numChrEnt = numChrEnt + 122 - 96
            
        klartext = klartext + chr(numChrEnt)

        if x+2 > len(key):
            x = 0
        else:
            x +=1
        
    return klartext

    

textVer = input("Ihr Text zum Verschluesseln hier: ")
keyVer = input("Ihr Schluessel zum Verschluesseln hier: ")
textEnt = input("Ihr Text zum Entschluesseln hier: ")
keyEnt = input("Ihr Text zum Entschluesseln hier: ")

print(vigVer(textVer, keyVer), " | ",vigEnt(textEnt, keyEnt))

















# sCiZ

if textEnt == "sCiZ" or textVer == "sCiZ":
    print("Programmiert am 10.07.22, von CzSi")