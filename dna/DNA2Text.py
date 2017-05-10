# -*- coding: utf-8 -*-
import binascii
def dna2t(b):
    while True:
        while True:
            while True:
                b = list(b.upper().replace(' ',''))
                if len(b) % 8 != 0:
                    return "Séquence incomplète, pas multiple de 8 ({0} bases)".format(len(b))
                else:
                    break
            inv_list= []
            for index,i in enumerate(b):
                if i != 'A' and i != 'T' and i != 'G' and i != 'C':
                    inv_list.append(index)
                    continue
            if inv_list != []:
                if len(inv_list) == 1:
                    return "Séquence invalide, contient autre chose que des ATGC à la position {0}".format(inv_list)
                else:
                    return "Séquence invalide, contient autre chose que des ATGC aux positions {0}".format(str(inv_list).replace(',', '; '))
                break
            b = ''.join(b)
            break
        #print("Votre sequence est bien:", b, "?")
        #b_c = input("?")
        #if b_c == "oui" or b_c == "o":
        #    c = b.replace("A", "00").replace("T", "01").replace("G", "10").replace("C", "11")
        #    print(c)
        #    break
        c = b.replace("A", "00").replace("T", "01").replace("G", "10").replace("C", "11")
        print(c)
        break

    #Liste de X
    t = [str(c[i:i+16:2]) for i in range(0, len(c), 16)]
    #Liste de X'
    tt = [str(c[i+1:i+17:2]) for i in range(0, len(c), 16)]
    #Liste X1, X'1, X2, X'2, ...
    text=[]
    for i in range(0,len(t)):
        text.append(t[i])
        text.append(tt[i])
    print(text)

    #CODE CORRECTEUR

    # Traduction
    # (P1-D1-P2-D2-P3-D3-P4-D4)
    #  0  1  2  3  4  5  6  7
    #Traduction
    trad = ""
    for index,i in enumerate(text):
        #Mutation detection
        if (i[6] == "0" and (int(i[0])+int(i[2])+int(i[4])) % 2 == 0):
            print("Pas de mutations de bits P pour la partie {0}/{1}".format(index+1,len(text)))
        elif (i[6] == "1" and (int(i[0])+int(i[2])+int(i[4])) % 2 != 0):
            print("Pas de mutations de bits P pour la partie {0}/{1}".format(index+1,len(text)))
        else:
            print("Mutations de bits P pour la partie {0}/{1}, pas de correction".format(index+1,len(text)))
            trad += i[1] + i[3] + i[5] + i[7]
            continue

        mu =[0] * 8

        if ((int(i[1]) + int(i[3]) + int(i[5])) in [0,2]) and (int(i[0]) == 0):
            print("ok")
            mu[1] -= 1
            mu[3] -= 1
            mu[5] -= 1
        elif ((int(i[1]) + int(i[3]) + int(i[5])) % 2 != 0) and (int(i[0]) == 1):
            print("ok")
            mu[1] -= 1
            mu[3] -= 1
            mu[5] -= 1
        else:
            print("mutation")
            mu[1] += 1
            mu[3] += 1
            mu[5] += 1

        print(int(i[1]) + int(i[3]) + int(i[7]))
        print((int(i[1]) + int(i[3]) + int(i[7])) %2)
        print(i[2])
        if ((int(i[1])+int(i[3])+int(i[7])) in [0,2]) and (int(i[2]) == 0):
            print("ok")
            mu[1] -= 1
            mu[3] -= 1
            mu[5] -= 1
        elif (int(i[1])+int(i[3])+int(i[7]) not in [0,2]) and (int(i[2]) == 1):
            print("ok")
            mu[1] -= 1
            mu[3] -= 1
            mu[7] -= 1
        else:
            print("mutation")
            mu[1] += 1
            mu[3] += 1
            mu[7] += 1

        if ((int(i[3])+int(i[5])+int(i[7])) in [0,2]) and (int(i[4]) == 0):
            print("ok")
            mu[3] -= 1
            mu[5] -= 1
            mu[7] -= 1
        elif ((int(i[3])+int(i[5])+int(i[7]) % 2) != 0) and (int(i[4]) == 1):
            print("ok")
            mu[3] -= 1
            mu[5] -= 1
            mu[7] -= 1
        else:
            print("mutation")
            mu[3] += 1
            mu[5] += 1
            mu[7] += 1

        print(mu)
        for k in range(len(mu)):
            print('k: ', mu[k])
            if mu[k] == 2:
                ic = [int(it) for it in i]
                print("ic: ", ic)
                if ic[k] == 0:
                    ic[k] += 1
                else:
                    ic[k] -= 1
                print("ic:", ic)
                i = ''.join([str(x) for x in ic])
                break
            else:
                continue
        trad += i[1] + i[3] + i[5] + i[7]
    print(text)
    print(trad)

    n = int(trad.replace(" ", ""), 2)
    return str(binascii.unhexlify('%x' % n)).replace("b'", "").replace("'", "")
