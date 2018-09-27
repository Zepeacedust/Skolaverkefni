import random
def conc(a):
    output = []
    for x in a:
        output.append(x)
    return output
text = open(input("veldu file: "), "r").read()
text = list(text)
pairdict = {"doodle":"shite"}
for x in range(len(text)):
    if text[x] in pairdict.keys():
        (pairdict[text[x]]).append(text[(x + 1) % len(text)])
        (pairdict[text[x]]).append(text[(x + 2) % len(text)])
        (pairdict[text[x]]).append(text[(x + 3) % len(text)])
        (pairdict[text[x]]).append(text[(x + 4) % len(text)])
    else:
        pairdict[text[x]] = [text[(x + 1) % len(text)], text[(x + 2) % len(text)], text[(x + 3) % len(text)], text[(x + 4) % len(text)]]
length = int(input("string length: "))
chain = [random.choice(text)]
for x in range(length):
    chain.append(
        random.choice(
            random.choice(
                pairdict[chain[-1]]
            )
        )
    )
print("".join(chain))