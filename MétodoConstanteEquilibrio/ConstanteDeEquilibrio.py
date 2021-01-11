import math
import numpy as np

global kList, K, cont, Zn, kNL, nT
kList = []
kNL = []
Zn = []
compL = []
rList = []
cont = 0


def calculoK(componente,P,T,zList):

    #global componente, P, T

    #T = ((T * 1.8) + 32)

    print(componente)
    print("T: ", T)
    if componente == 1:

        #Metano
        A0 = 1.636
        A1 = 0
        A2 = 0
        A3 = 31.6621
        A4 = -49.3534
        A5 = 0.00000531
        A6 = 0
        A7 = 0
        A8 = 0.128525
        A9 = -0.78338
        A10 = 0
        A11 = 0
        A12 = 0
        A13 = -5.3569
        A14 = 0
        A15 = -0.00000023
        A16 = -0.00000002
        A17 = 0

        Km = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
        + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
        print("Km = ",Km)

        kList.append(Km)

    if componente == 2:

        #Etano
        A0 = 6.41934
        A1 = 0
        A2 = 0
        A3 = -290.83
        A4 = 2629.1
        A5 = 0
        A6 = 0
        A7 = 0.00000009
        A8 = 0.129759
        A9 = -1.19703
        A10 = -84600
        A11 = -71.0352
        A12 = 0.596404
        A13 = -4.7437
        A14 = 78200
        A15 = 0
        A16 = 0
        A17 = 0

        Ke = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
        + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
        print("Ke = ", Ke)

        kList.append(Ke)

    if componente == 3:

        #Propano
        A0 = -7.8499
        A1 = 0
        A2 = 0
        A3 = 47.056
        A4 = 0
        A5 = -0.00000117
        A6 = 0.0007145
        A7 = 0
        A8 = 0
        A9 = 0.12348
        A10 = 16690
        A11 = 0
        A12 = 0.23319
        A13 = 0
        A14 = -44800
        A15 = 0.0000055
        A16 = 0
        A17 = 0

        Kp = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
        + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
        print("Kp = ",Kp)
        kList.append(Kp)

    if componente == 4:

        #Isobutano
        A0 = -2.17137
        A1 = 0
        A2 = 0
        A3 = 0
        A4 = 0
        A5 = 0
        A6 = 0.001254
        A7 = 0.00000001
        A8 = 0.166097
        A9 = -2.75945
        A10 = 0
        A11 = 0
        A12 = 0
        A13 = 0
        A14 = -884
        A15 = 0
        A16 = -0.00000057
        A17 = -0.00000001

        Kib = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
        + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
        print(Kib)
        kList.append(Kib)

    if componente == 5:

        #n-Butano
        A0 = 37.211
        A1 = 0.86564
        A2 = 0
        A3 = 732.2
        A4 = 0
        A5 = 0
        A6 = 0
        A7 = 0.00000937
        A8 = -1.07657
        A9 = 0
        A10 = 0
        A11 = -66.221
        A12 = 0
        A13 = 0
        A14 = 917000
        A15 = 0
        A16 = 0.00000498
        A17 = -0.00000126

        Knb = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
        + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
        print(Knb)
        kList.append(Knb)

    if componente == 13:

        #CO2
        A0 = 9.0242
        A1 = 0
        A2 = 0
        A3 = -207.033
        A4 = 0
        A5 = 0.0000466
        A6 = -0.006992
        A7 = 0.00000289
        A8 = -0.006223
        A9 = 0
        A10 = 0
        A11 = 0
        A12 = 0.27098
        A13 = 0
        A14 = 0
        A15 = 0.0000882
        A16 = 0.00000255
        A17 = 0

        Kco2 = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
        + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
        print(Kco2)
        kList.append(Kco2)

    if componente == 14:
        
        #H2S
        A0 = -4.7071
        A1 = 0.061982
        A2 = 0
        A3 = 82.627
        A4 = 0
        A5 = -0.00000739
        A6 = 0
        A7 = 0
        A8 = 0.240869
        A9 = -0.64405
        A10 = 0
        A11 = 0
        A12 = 0
        A13 = -12.704
        A14 = 0
        A15 = -0.0000013
        A16 = 0
        A17 = 0

        Kh2s = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
        + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
        print(Kh2s)
        kList.append(Kh2s)

    if componente == 18:

        #N2
        A0 = 1.78857
        A1 = 0
        A2 = -0.001356
        A3 = -6.187
        A4 = 0
        A5 = 0
        A6 = 0
        A7 = 0.00000025
        A8 = 0
        A9 = 0
        A10 = 0
        A11 = 0
        A12 = 0
        A13 = 0
        A14 = 5870000
        A15 = 0
        A16 = 0.00000001
        A17 = 0.00000011

        Kn2 = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
        + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
        print(Kn2)
        kList.append(Kn2)

    if cont >=1:
        criterio(P,T,zList)
    
def criterio(P,T,zList,componente):

    ksum = 0
    zsum = 0
    K = 0

    print("Kl = ",kList)
    print("Zl = ", Zn)

    for g in range(len(zList)):
        if zList[g] != 0 and zList[g] not in Zn:
            Zn.append(zList[g])


        
    for l in range(len(kList)):

        #print("Zln = ", Zn)
        #ksum += kList[l]
        #zsum += Zn[l]
        Kdiv = Zn[l]/kList[l]
        print("Kdiv: ", Kdiv)
        K += Kdiv
        print("K+Kdiv: ", K)
        #print("K",K)

    print("K1: ", K)


    #print("ksum: ", ksum)
    #print("zsum: ", zsum)
#########

    if K > 1 :

        while K >= 1:

            T += 0.01
            print("nT: ", T)
            #newK(componente, P ,T, Zn)
            print("K+: " , K)
            print("Z", Zn)
            kNL.clear()
            rList.clear()

            if 0 in componente:

                    #Metano
                    A0 = 1.636
                    A1 = 0
                    A2 = 0
                    A3 = 31.6621
                    A4 = -49.3534
                    A5 = 0.00000531
                    A6 = 0
                    A7 = 0
                    A8 = 0.128525
                    A9 = -0.78338
                    A10 = 0
                    A11 = 0
                    A12 = 0
                    A13 = -5.3569
                    A14 = 0
                    A15 = -0.00000023
                    A16 = -0.00000002
                    A17 = 0

                    Kmi = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
                    + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
                    print("Kmi = ",Kmi)

                    kNL.append(Kmi)

            if 1 in componente:

                #Etano
                A0 = 6.41934
                A1 = 0
                A2 = 0
                A3 = -290.83
                A4 = 2629.1
                A5 = 0
                A6 = 0
                A7 = 0.00000009
                A8 = 0.129759
                A9 = -1.19703
                A10 = -84600
                A11 = -71.0352
                A12 = 0.596404
                A13 = -4.7437
                A14 = 78200
                A15 = 0
                A16 = 0
                A17 = 0

                Kei = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
                + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
                print("Kei = ", Kei)

                kNL.append(Kei)

            if 2 in componente:

                #Propano
                A0 = -7.8499
                A1 = 0
                A2 = 0
                A3 = 47.056
                A4 = 0
                A5 = -0.00000117
                A6 = 0.0007145
                A7 = 0
                A8 = 0
                A9 = 0.12348
                A10 = 16690
                A11 = 0
                A12 = 0.23319
                A13 = 0
                A14 = -44800
                A15 = 0.0000055
                A16 = 0
                A17 = 0

                Kpi = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
                + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
                print("Kpi = ",Kpi)
                kNL.append(Kpi)

            if 4 in componente:

                #Isobutano
                A0 = -2.17137
                A1 = 0
                A2 = 0
                A3 = 0
                A4 = 0
                A5 = 0
                A6 = 0.001254
                A7 = 0.00000001
                A8 = 0.166097
                A9 = -2.75945
                A10 = 0
                A11 = 0
                A12 = 0
                A13 = 0
                A14 = -884
                A15 = 0
                A16 = -0.00000057
                A17 = -0.00000001

                Kibi = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
                + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
                print(Kibi)
                kNL.append(Kibi)

            if componente == 5:

                #n-Butano
                A0 = 37.211
                A1 = 0.86564
                A2 = 0
                A3 = 732.2
                A4 = 0
                A5 = 0
                A6 = 0
                A7 = 0.00000937
                A8 = -1.07657
                A9 = 0
                A10 = 0
                A11 = -66.221
                A12 = 0
                A13 = 0
                A14 = 917000
                A15 = 0
                A16 = 0.00000498
                A17 = -0.00000126

                Knbi = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
                + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
                print(Knbi)
                kNL.append(Knbi)

            if componente == 13:

                #CO2
                A0 = 9.0242
                A1 = 0
                A2 = 0
                A3 = -207.033
                A4 = 0
                A5 = 0.0000466
                A6 = -0.006992
                A7 = 0.00000289
                A8 = -0.006223
                A9 = 0
                A10 = 0
                A11 = 0
                A12 = 0.27098
                A13 = 0
                A14 = 0
                A15 = 0.0000882
                A16 = 0.00000255
                A17 = 0

                Kco2i = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
                + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
                print(Kco2i)
                kNL.append(Kco2i)

            if componente == 14:
                
                #H2S
                A0 = -4.7071
                A1 = 0.061982
                A2 = 0
                A3 = 82.627
                A4 = 0
                A5 = -0.00000739
                A6 = 0
                A7 = 0
                A8 = 0.240869
                A9 = -0.64405
                A10 = 0
                A11 = 0
                A12 = 0
                A13 = -12.704
                A14 = 0
                A15 = -0.0000013
                A16 = 0
                A17 = 0

                Kh2si = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
                + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
                print(Kh2si)
                kNL.append(Kh2si)

            if componente == 18:

                #N2
                A0 = 1.78857
                A1 = 0
                A2 = -0.001356
                A3 = -6.187
                A4 = 0
                A5 = 0
                A6 = 0
                A7 = 0.00000025
                A8 = 0
                A9 = 0
                A10 = 0
                A11 = 0
                A12 = 0
                A13 = 0
                A14 = 5870000
                A15 = 0
                A16 = 0.00000001
                A17 = 0.00000011

                Kn2i = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
                + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
                print(Kn2i)
                kNL.append(Kn2i)
            
            K = 0

            for l in range(len(kList)):

                #print("Zln = ", Zn)
                #ksum += kList[l]
                #zsum += Zn[l]
                Kdiv = Zn[l]/kNL[l]
                K += Kdiv

                    #print("K",K)
            
            print("Ki+: ", K)
            nT = T
            print(nT)
            rList.append(K)
            rList.append(nT)
            #kList.clear()
            #Zn.clear()


    elif K < 1:

        while K <= 1:
            T -= 0.01
            print("nT: ", T)
            #newK(componente, P, T, Zn)
            print("K-: " , K)
            print("Com: ", componente)

            global cont
            cont += 1
            #if 1<= cont < 11:
            #calculoK(componente,P,T,Zn)
            print("cont",cont)
            #kList.clear()
            kNL.clear()
            rList.clear()

            if 0 in componente:

                #Metano
                A0 = 1.636
                A1 = 0
                A2 = 0
                A3 = 31.6621
                A4 = -49.3534
                A5 = 0.00000531
                A6 = 0
                A7 = 0
                A8 = 0.128525
                A9 = -0.78338
                A10 = 0
                A11 = 0
                A12 = 0
                A13 = -5.3569
                A14 = 0
                A15 = -0.00000023
                A16 = -0.00000002
                A17 = 0

                Kmi = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
                + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
                print("Kmi = ",Kmi)

                kNL.append(Kmi)

            if 1 in componente:

                #Etano
                A0 = 6.41934
                A1 = 0
                A2 = 0
                A3 = -290.83
                A4 = 2629.1
                A5 = 0
                A6 = 0
                A7 = 0.00000009
                A8 = 0.129759
                A9 = -1.19703
                A10 = -84600
                A11 = -71.0352
                A12 = 0.596404
                A13 = -4.7437
                A14 = 78200
                A15 = 0
                A16 = 0
                A17 = 0

                Kei = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
                + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
                print("Kei = ", Kei)

                kNL.append(Kei)

            if 2 in componente:

                #Propano
                A0 = -7.8499
                A1 = 0
                A2 = 0
                A3 = 47.056
                A4 = 0
                A5 = -0.00000117
                A6 = 0.0007145
                A7 = 0
                A8 = 0
                A9 = 0.12348
                A10 = 16690
                A11 = 0
                A12 = 0.23319
                A13 = 0
                A14 = -44800
                A15 = 0.0000055
                A16 = 0
                A17 = 0

                Kpi = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
                + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
                print("Kpi = ",Kpi)
                kNL.append(Kpi)

            if 4 in componente:

                #Isobutano
                A0 = -2.17137
                A1 = 0
                A2 = 0
                A3 = 0
                A4 = 0
                A5 = 0
                A6 = 0.001254
                A7 = 0.00000001
                A8 = 0.166097
                A9 = -2.75945
                A10 = 0
                A11 = 0
                A12 = 0
                A13 = 0
                A14 = -884
                A15 = 0
                A16 = -0.00000057
                A17 = -0.00000001

                Kibi = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
                + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
                print(Kibi)
                kNL.append(Kibi)

            if componente == 5:

                #n-Butano
                A0 = 37.211
                A1 = 0.86564
                A2 = 0
                A3 = 732.2
                A4 = 0
                A5 = 0
                A6 = 0
                A7 = 0.00000937
                A8 = -1.07657
                A9 = 0
                A10 = 0
                A11 = -66.221
                A12 = 0
                A13 = 0
                A14 = 917000
                A15 = 0
                A16 = 0.00000498
                A17 = -0.00000126

                Knbi = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
                + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
                print(Knbi)
                kNL.append(Knbi)

            if componente == 13:

                #CO2
                A0 = 9.0242
                A1 = 0
                A2 = 0
                A3 = -207.033
                A4 = 0
                A5 = 0.0000466
                A6 = -0.006992
                A7 = 0.00000289
                A8 = -0.006223
                A9 = 0
                A10 = 0
                A11 = 0
                A12 = 0.27098
                A13 = 0
                A14 = 0
                A15 = 0.0000882
                A16 = 0.00000255
                A17 = 0

                Kco2i = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
                + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
                print(Kco2i)
                kNL.append(Kco2i)

            if componente == 14:
                
                #H2S
                A0 = -4.7071
                A1 = 0.061982
                A2 = 0
                A3 = 82.627
                A4 = 0
                A5 = -0.00000739
                A6 = 0
                A7 = 0
                A8 = 0.240869
                A9 = -0.64405
                A10 = 0
                A11 = 0
                A12 = 0
                A13 = -12.704
                A14 = 0
                A15 = -0.0000013
                A16 = 0
                A17 = 0

                Kh2si = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
                + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
                print(Kh2si)
                kNL.append(Kh2si)

            if componente == 18:

                #N2
                A0 = 1.78857
                A1 = 0
                A2 = -0.001356
                A3 = -6.187
                A4 = 0
                A5 = 0
                A6 = 0
                A7 = 0.00000025
                A8 = 0
                A9 = 0
                A10 = 0
                A11 = 0
                A12 = 0
                A13 = 0
                A14 = 5870000
                A15 = 0
                A16 = 0.00000001
                A17 = 0.00000011

                Kn2i = (A0 + (A1*T) + (A2*P) + (A3*(T**(-1))) + (A4/P) + (A5*P*T) + (A6*(T**2)) + (A7*(P**2)) + (A8*(P/T)) + (A9 * math.log(P/T)) + (A10*(P**(-2)))
                + (A11*(T/P)) + (A12*((T**2)/P)) + (A13*(P/(T**2))) + (A14*(T/(P**3))) + (A15*(T**3)) + (A16*((P**3)/(T**2))) + (A17*(T**4)))
                print(Kn2i)
                kNL.append(Kn2i)
            
            K = 0

            for l in range(len(kList)):

                Kdiv = Zn[l]/kNL[l]
                K += Kdiv

                    #print("K",K)

            print("Ki-: ", K)
            nT = T
            print(nT)
            rList.append(K)
            rList.append(nT)
            
    return rList

#calculoK(1)