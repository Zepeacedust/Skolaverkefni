number = input("number to be converted: ")
output = ""
for digit in list(str(number)):
    if digit.upper in ["A","B","C","D","E","F"]:
        character_number = ["A","B","C","D","E","F"].index(digit) + 10
    else:
        character_number = int(digit)
    output += ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"][character_number]
number = output
output = 0
for x in range(len(number)):
    output += int(number[x]) * (2 ** (len(number) - (x + 1)))
print(output)