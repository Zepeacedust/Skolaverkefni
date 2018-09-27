#Arnór friðrikkson
print("liður 1")
tala1 = int(input("skráðu inn eina heiltölu: "))#setja tala 1 að tölu sem notandi velur
tala2 = int(input("skráðu inn seinni heiltölu: "))#setja tala 1 að tölu sem notandi velur
if tala1 == tala2:#ef þetta eru ssömu tölur halda áfram
    print("þetta eru sömu tölurnar")#prenta "þetta eru ömu tölur"
else:#ef þær eru ekki sama talan halda áfram
    print("%i er stærri" % (max(tala1, tala2)))#nota inbuilt functuinið max til að fæ stærri töluna
print("liður 2")
manudir = ["janúar", "febrúar", "mars", "apríl", "mæi", "júní", "júlí", "ágúst", "september", "óktóber", "nóvember", "desember"]#gera lista af öllum mánuðunum í réttri röð
manudur = input("veldu mánuð: ").lower()
if manudur in manudir:#passa að valið sé í listanum af mánuðum
    print("þú valdur mánuð númer %i" % (manudir.index(manudur) + 1))#fá hvaða index valdi mánuðurinn er og prenta það
else:#ef inputtið er ekki mánuður
    print("þú valdir ekki mańuð")# segja að það er ekki mánuður
print("liður 3")
#fara efti aldursbilum og prenta mismunadni hluti
aldur = int(input("hversu gamall/gömul ert þú?"))#spurja hversu gamall notandinn er
if aldur <= 6 and aldur >= 0:
    print("þá ættir þú að fara í skóla")
elif aldur < 16:
    kostur = input("ætlar þú í framhaldsskóla?")
    if kostur == "J":
        print("það er gott")
    elif kostur == "N":
        print("þú ættir að gera það")
elif aldur < 106:
    print("gangi þér vel í lífinu")
else:
    print("þetta er ekki venjulegt svar")
print("liður 4")
tala1 = int(input("veldu tölu á milli 0 og 25"))
if tala1 < 0 or tala1 > 25:
    print("þetta er ekki rétt")
else:
    print(tala1 * 1.7)
print("liður 5")
brandari = input("villtu brandara?")
if brandari == "já":
    print("afhverju var hafnarstjórinn rekinn?\n hann vildi ekki taka við skipunum!")
else:
    print(" 0   0 ")
    print("       ")
    print(" 00000 ")
    print("0     0")