val = 4
while val != 0:
    print("=+=Valmynd=+=")
    print("1.")
    print("2.")
    print("3.")
    print("0. Hætta")
    print("=+=Valmynd=+=")
    val = int(input("Veldu :"))
    validerror = 1

    if val == 1:
        print("=1=")
        num11 = int(input("Sláðu inn númer : "))
        num12 = int(input("Sláðu inn næsta númerið : "))
        num13 = num11*num12
        num14 = num11+num12
        print("Samanloögð =",num14)
        print("Margfölduð =",num13)
        validerror = 0

    if val == 2:
        print("=2=")
        nafn21 = input("Fornafn? :")
        nafn22 = input("Eftirnafn? :")
        print("Halló",nafn21,nafn22)
        validerror = 0

    if val == 3:
        upp3 = 0
        low3 = 0
        spe3 = 0
        t31 = ""
        t32 = ""
        print("=3=")
        mtext3 = input("Sláðu inn texta : ")
        for charac in mtext3:
            if charac.isupper():
                upp3 += 1
            if charac.islower():
                low3 += 1
        print("Fjöldi hástafi : ", upp3)
        print("Fjöldi lágstafi : ", low3)
        



        validerror = 0


    if val == 0:
        validerror = 0
        exit()


    if validerror == 1:
        print("!!! Ekki rétt númer !!!")