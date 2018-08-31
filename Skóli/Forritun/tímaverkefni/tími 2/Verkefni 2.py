tolur =[]
for x in range(3):
    tolur.append(int(input("skráðu inn tölu %i: " % (x + 1))))#for loop sem appendar svari á lista
print("summa talnanna er %i" % (sum(tolur)))#prentar summuna inni í stringnum með því að skipt aút
print("margfeldi talnanna er %i" % (tolur[0] * tolur[1] * tolur[2]))
print("frádráttur talnanna er %i" % (tolur[0] - tolur[1] - tolur[2]))