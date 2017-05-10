# -*- coding: utf-8 -*-
import binascii
def t2dna(t):
    #t = bytearray(str(input("Texte?")), 'utf8')
    t = bytearray(str(t), 'utf8')
    h = binascii.hexlify(t)
    print(str(h).replace("b","").replace("'",""))
    b = bin(int(h, 16)).replace('b','') #On enlève le b, signe de binaire
    print(b)

    c = [str(b[i:i+8]) for i in range(0, len(b), 8)]
    print(c)
    ecc= ""
    for i in c:
        if (int(i[0])+int(i[1])+int(i[2])) % 2 == 0: #i[0] P1
            ecc += "0"
            x = 0
        else:
            ecc += "1"
            x = 1
        if (int(i[4])+int(i[5])+int(i[6])) % 2 == 0: #i[1] P'1
            ecc += "0"
            y = 0
        else:
            ecc += "1"
            y = 1
        ecc += i[0] #i[2] D1
        ecc += i[4] #i[3] D'1

        if (int(i[0])+int(i[1])+int(i[3])) % 2 == 0: #i[4] P2
            ecc += "0"
            x += 0
        else:
            ecc += "1"
            x += 1
        if (int(i[4])+int(i[5])+int(i[7])) % 2 == 0: #i[5] P'2
            ecc += "0"
            y += 0
        else:
            ecc += "1"
            y += 1
        ecc += i[1] #i[6] D2
        ecc += i[5] #i[7] D'2

        if (int(i[1])+int(i[2])+int(i[3])) % 2 == 0: #i[8] P3
            ecc += "0"
            x += 0
        else:
            ecc += "1"
            x += 1
        if (int(i[5])+int(i[6])+int(i[7])) % 2 == 0: #i[9] P'3
            ecc += "0"
            y += 0
        else:
            ecc += "1"
            y += 1
        ecc += i[2] #i[10] D3
        ecc += i[6] #i[11] D'3

        if x % 2 == 0: #i[6] P4
            ecc += "0"
        else:
            ecc += "1"
        if y % 2 == 0: #i[6] P'4
            ecc += "0"
        else:
            ecc += "1"
        ecc += i[3] #i[7] D4
        ecc += i[7] #i[7] D'4
    #Séquence --> P1-P'1-D1-D'1-P2-P'2-D2-D'2-P3-P'3-D3-D'3-P4-P'4-D4-D'4
    print(ecc)

    g = [ecc[i:i+2] for i in range(0, len(ecc), 2)]
    dna = ""
    for i in g:
        if i == "00":
            dna += "A"
        elif i == "01":
            dna += "T"
        elif i == "10":
            dna += "G"
        elif i == "11":
            dna += "C"
    dna = ' '.join([dna[i:i+8] for i in range(0, len(dna), 8)])
    return dna
