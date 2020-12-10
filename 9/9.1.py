import re

input_file = open('input')
input = []

preamble = 25

for number in input_file:
    number = int(re.search('\d+',number).group())
    input.append(number)

for i in range(preamble,len(input)):
    valid = False
    for j in range(i-preamble,i):
        for k in range(i-preamble,i):
            if k != j:
                if input[k]+input[j] == input[i]:
                    valid = True
    if not valid:
        print(f'{input[i]}')
