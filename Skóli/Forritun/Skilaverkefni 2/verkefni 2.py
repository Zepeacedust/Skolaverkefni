#arnór friðriksson 7/9
print("veldu eitt ef þú vilt fá lið eitt")
print("veldu tvö ef þú vilt fá lið tvö")
print("veldu þrjú ef þú vilt fá lið þrjú")
print("veldu fjögur ef þú vilt fá lið fjögur")
print("veldu fimm ef þú vilt fá lið fimm")
print("veldu eithvað annað til að hætta")
liður = input()#setja upp valmynd
if liður == "1":#fyrsti liður í valmyndinni
    tala1 = int(input("veldu fyrstu tölu: "))
    tala2 = int(input("veldu aðra töluna: "))
    tala3 = int(input("veldu seinustu töluna: "))#setja tölurnar þrjár
    if not(tala1 == tala2 or tala2 == tala3 or tala1 == tala3):#passa að það séu ekki tvær eins tölur
        if tala1 < tala2 and tala1 > tala3 or tala1 < tala2 and tala1 > tala3:
            print("miðjan er ", tala1)#gá hvort tala 1 sé rétt
        elif tala2 > tala1 and tala2 < tala3 or tala2 < tala1 and tala2 > tala3:
            print("miðjan er ", tala2)#gá hvort tala 2 sé rétt
        elif tala3 > tala1 and tala3 < tala2 or tala3 < tala1 and tala3 > tala2:
            print("miðjan er ", tala3)#gá hvort tala 3 sé rétt
    else: print("það má ekki nota sömu tölu oftar en einu sinni")
elif liður == "2":#seinni liður í valmmyndinni
    lengd = int(input("veldu lengd: "))#fá lengd til að breyta
    tommur_or_Cent = input("T fyrir tommur C fyrir centimetra:\n")# velja hvort inputtið sé í tommum eða centimetrum
    if tommur_or_Cent == "T":
        print("það eru %f centimetrar" % (lengd * 2.52))#margfalda með 2.52 til á fá cm
    elif tommur_or_Cent == "C":
        print("það eru %f tommur" % (lengd / 2.52))#deila með 2.52 til að fá timmur
elif liður == "3":#þriðji liður í valmynd
    manudur = int(input("veldu mánuð: "))
    if manudur > 12 or manudur < 1:
        print("Rangur innsláttur")
    elif manudur < 4:# case 1 á listanum: 1-3
        print("nú er dagurinn farinn að lengjast") 
    elif manudur < 6:#case 2 á listanum: 4-5
        print("nú er vorið komið og grundirnar gróa")
    elif manudur < 9:#case 3 á listnanum: 6-8
        print("núna er sumarið komið með blóm í haga")
    elif manudur < 12:#case 4 á listanum: 9-11
        print("nú er haustið gengið í garð")
    elif manudur == 12:#case 5 á listanim: 12
        print("nú fer að styttast í jólin")
    else: print("þetta á aldrei að gerast, vinsamlegast sentu email á arnor0903@gmail.com með lýsingu á mánaðarnúmeri")
elif liður == "4":#fjórði liður á valmynd
    nafn = input("hvað heitir þú? ")
    kyn = input("hvaða kyn ert þú? ").lower()
    tala1 = int(input("veldu fyrstu töluna: "))
    tala2 = int(input("veldu seinni töluna: "))#finna kyn, nafnt og tvær tölurnar
    if kyn == "kk": print("blessaður %s" % (nafn))
    elif kyn == "kvk": print("blessuð %s" % (nafn))
    else: print("Blessaður eða blessuð ég veit ekki hvors kyns þú ert")
    if tala1 == tala2: #passa að þetta séu ekki sama tala
        print("tölurnar tvær eru sama tala")
    elif 100 < abs(tala1 - tala2):
        print("mismunur á milli þessara talna er meira en 100")#prentahvort munirinn sé meiri en 100
    elif 100 > abs(tala1 - tala2):#
        print("mismunur á milli þessara talna er minni en 100")#prenta hvort mismuruinn sé minni en 100
    else:
        print("mismunur þessara talna er 100")#prenta ef mismunurinn sé 100
elif liður == "5":#fimmti liður á valmynd
    tala1 = int(input("veldu tölu sem er stærri en 10 eða minni en 0: "))
    if tala1 > 10 or tala1 <0:
        print("vel gert")
    else: print("%i er ekki tala stærri en 10 eða minni en 0" % (tala1))