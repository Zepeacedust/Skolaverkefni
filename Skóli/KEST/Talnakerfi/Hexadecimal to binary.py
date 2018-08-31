number = input("number to be converted: ")
output = ""
for digit in list(str(number)):
    if digit in ["A","B","C","D","E","F"]:
        character_number = ["A","B","C","D","E","F"].index(digit) + 10
    else:
        character_number = int(digit)
    output += ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"][character_number]
print(output)
