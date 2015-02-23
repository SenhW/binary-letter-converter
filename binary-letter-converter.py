import sys

input_string = ''.join(sys.argv[1:])
binary = [input_string[i: i + 8] for i in range(0, len(input_string), 8)]
output = ''
for binary_letter in binary:
    output += chr(int(binary_letter, 2))
print(output)