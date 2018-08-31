number = str(input("number to be converted: "))
output = 0
for x in range(len(number)):
    output += int(number[x]) * (2 ** (len(number) - (x + 1)))
print(output)