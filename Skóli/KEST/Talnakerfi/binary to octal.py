number = input("number to be converted: ")
output = 0
if not(len(number) % 3 == 0):
    number = (3 - len(number) % 3) * "0" + number
for x in range(0,len(number), 3):
    output *= 10
    output += ["000", "001", "010", "011", "100", "101", "110", "111"].index(number[x:x+3])
print(output) 