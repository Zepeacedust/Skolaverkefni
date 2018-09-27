# Arnór Wed Sep 19 10:38:46 2018
from math import pi#iporta pi fyrir lið 4.2 pg 4.3
proceed = True
while proceed:
   #setja upp valmynd
    print('veldu 1 fyrir lið 1')
    print('veldu 2 fyrir lið 2')
    print('veldu 3 fyrir lið 3')
    print('veldu 4 fyrir lið 4')
    print('veldu exit til að hætta')
    liður = input()
    if liður == '1':
        #biður um nafn skónúmer og búð, notar aðeins nýlegra formatting en ég hef notað áður
        nafn = input("hvað heitir þú? ")
        skonumer = input("hvaða skónúmer notar þú? ")
        bud = input("í hvaða skóbúð verslar þú oftast? ")
        print("Góðan dag {nafn}, þú notar skónumer {numer} og verslar oftast í skóbúðinni {bud}.".format(nafn = nafn, numer = skonumer, bud = bud))
    elif liður == '2':
        #biður um stigafjölda og prentar mismunandi wtrings eftir  því
        stig = int(input("hveru mörg stig voru skoruð í handboltaleiknum? "))
        if stig >= 17: print("vel gert")
        elif stig < 17: print("Það gengur betur næst")
        if stig > 35: print("voru þeir einir á vellinum?")
    elif liður == '3':
        #tekur inn þrhár tölur og botar þær í formúlinni sem er neðar
        tala1 = int(input("veldu tölu 1: "))
        tala2 = int(input("veldu tölu 2: "))
        tala3 = int(input("veldu tölu 3: "))
        print("({tala1} + {tala2}) - {tala3} = {tala4}".format(
        tala1 = tala1,
        tala2 = tala2,
        tala3 = tala3,
        tala4 = tala1+tala2-tala3))

    elif liður == '4':
        reikn = input("veldu 1 fyrir ummál ferhyrning\nveldu 2 fyrir rúmmál sívalings\nveldur 3 fyrir flatarmál hrings\n")#smá löng valmynd, væri hægt að skipta'á aðrar línur
        if reikn == "1":#ef maður velur kassa biðja um lengd og breidd og prenta svarið
            lengd = int(input("lengd: "))
            breidd = int(input("breidd: "))
            print("ummálið er {umm}".format(umm = lengd * 2 + breidd * 2))
        elif reikn == "2":#ef mapur biður um sívaling biðja im radíus og hæð og prenta svarið
            radius = int(input("hver er radíus botnhringsins"))
            hed = int(input("hver er hæð sívalingsins"))
            print("rúmmálið er {rumm}".format(rumm = radius ** 2 * pi * hed))
        elif reikn == "3":#ef maður velur hring biðja um radíus og prenta svarið
            radius = int(input("hver er radíus hringsins: "))
            print("flatarmálið er {flat}".format(flat = radius ** 2 * pi))
    elif liður == 'exit': proceed = False# exit condition