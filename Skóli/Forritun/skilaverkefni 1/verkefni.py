#Arnór friðriksson 29 ágúst
nafn = input("hvað heitir þú? ")
print("Velkomin í áfangann FOR1A3U %s. Þetta verður skemmtileg önn, ég hlakka til að læra forritun." % (nafn)) # biðja um og prenta nafn notandans


tala1 = float(input("veldu kommutölu með 3 aukastögum: "))
print("þú valdir %i" % (round(tala1, 1)))


tala1 = int(input("veldu fyrri heiltölu: "))
tala2 = int(input("veldu seinni heiltölu: "))
print(tala1 * tala2)#margfalda tölu 1 og tölu 2
print(tala1 - tala2)#mínusa tölu 2 við tölu 1 


tala1 = int(input("sláðu inn hæð kassa: "))
tala2 = int(input("sláðu inn breidd kassa: "))
tala3 = int(input("sláðu inn lengd kassa: "))
print("rúmmál kassans er %i" % (tala1 * tala2 * tala3))# prenta og margfalda tölurnar þrjár


notenda_aldur = int(input("hversu gamall/gömul ert þú? "))
pabba_aldur= int(input("hversu gamall er pabbi þinn? "))
print("pabbi þinn var %i ára gamall þegar þú fæddist" % (pabba_aldur - notenda_aldur))# prenta aldur pabbsnd mínus aldur notandsans


tala1 = int(input("skráðu aldur fyrstu: "))
tala2 = int(input("skráðu aldur seinni: "))
tala3 = int(input("skráðu aldurþriðju manneskunnar: "))
print("meðalaldurinn er %f." % (tala1 + tala2 + tala3))#finna og prenta meðalal talna 1-3 

print("Gaman að geta aðstoðað þig við þessa útreikninga -%s-" % (nafn)) #prenta nafn og kveðja notanda