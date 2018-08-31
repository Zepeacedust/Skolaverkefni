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
if length >= 0: output += (int(length) +1) * "0"
print(output)