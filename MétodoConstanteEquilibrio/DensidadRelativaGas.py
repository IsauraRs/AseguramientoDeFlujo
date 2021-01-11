Ma = 28.96
global Mi, Zi
Mi = []
Zi = []


def miSum(elemsList):

    global MM
    MM = 0

    #print(elemsList)
    if 0 in elemsList:
        print("Met")

        Mi.append(16.043)
    
    if 1 in elemsList:

        Mi.append(30.07)

    if 2 in elemsList:
        Mi.append(44.0970)

    if 3 in elemsList:
        Mi.append(58.1230) 

    if 4 in elemsList:

        Mi.append(58.1230)

    if 5 in elemsList:

        Mi.append(72.15)

    if 6 in elemsList:

        Mi.append(72.15)

    if 7 in elemsList:

        Mi.append(86.177)

    if 8 in elemsList:
         
        Mi.append(100.204)

    if 9 in elemsList:

        Mi.append(114.231) 

    if 10 in elemsList:

        Mi.append(128.258)

    if 11 in elemsList:

        Mi.append(142.285)

    if 12 in elemsList:

        Mi.append(44.01)

    if 13 in elemsList:

        Mi.append(34.08)

    if 14 in elemsList:

        Mi.append(64.06)

    if 15 in elemsList:

        Mi.append(2.0159)
    
    if 16 in elemsList:

        Mi.append(31.9988)

    if 17 in elemsList:

        Mi.append(28.0134)

    if 18 in elemsList:

        Mi.append(36.4600)

def rog(Zi):
    
    mult = 0

    for t in range(len(Mi)):
        
        sigmma = (Zi[t] * Mi[t])
        mult += sigmma

    rogas = (mult/Ma)

    print(rogas)