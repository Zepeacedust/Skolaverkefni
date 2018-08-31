number = input("number to be converted: ")
output = ""
for x in number:
    output += ["000", "001", "010", "011", "100", "101", "110", "111"][int(x)]
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