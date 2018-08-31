number = input("number to be converted: ")
output = ""
for x in number:
    output += ["000", "001", "010", "011", "100", "101", "110", "111"][int(x)]


number = output
output = 0
for x in range(len(number)):
    output += int(number[x]) * (2 ** (len(number) - (x + 1)))
print(output)