import math
number = int(input("Number to be converted: "))
length = math.floor(math.log(number, 2))
output = ""
while number > 0:
    if number - 2 ** length >= 0:
        number -= 2 ** length
        output += "1"
        length -= 1
    else:
        output += "0"
        length -= 1
if length == 0: output += (int(length) +1) * "0"
number = output
output = 0
number = (3 -len(number) % 3) * "0" + number
for x in range(0,len(number), 3):
    output *= 10
    output = output + ["000", "001", "010", "011", "100", "101", "110", "111"].index(number[x:x+3])
print(output)