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
if l+ength >= 0: output += (int(length) + 1) * "0"
number = output
output = ""
if not(len(number) % 4 == 0):
    number = (4 - len(number) % 4) * "0" + number#passa að 
for x in range(0,len(number), 4):
    character_number = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"].index(number[x:x+4])
    if character_number >9:
        output += ["A","B","C","D","E","F"][character_number - 10]
    else:
        output += str(character_number)
print(output)