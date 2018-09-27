# Arnór Wed Sep 26 10:58:30 2018
import random
proceed = 'já'
while proceed == 'já':
    liður = input()
    print(liður)
    proceed = input("viltu halda áfram? ")

tala = random.randint(1,10)
svarað = False
while not svarað:
    if int(input("giskaðu tölu")) == tala: 
        svarað = True
        print("rétt svar")
    else: print("rangt svar reyndu aftur")

tala = 0
while tala < 11:
    if tala == 3 or tala == 6:
    else:
        print(tala)
    tala += 1


tala = 2
while tala < 10:
    print(tala)
    tala += 2
tala2 = tala = 0 
while tala < 6:
    print("*****")