number = input("number to be converted: ")
output = ""
for x in number:
    output += ["000", "001", "010", "011", "100", "101", "110", "111"][int(x)]
print(output)