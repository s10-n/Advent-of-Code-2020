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
        target_number = input[i]
       
for i in range(len(input)):
    addends = []
    test_sum = input[i]
    addends.append(input[i])
    for j in range(i+1,len(input)):
        if test_sum == target_number and input[i] != target_number:
            addends.sort()
            print(addends[0]+addends[-1])
            break
        elif test_sum < target_number:
            test_sum += input[j]
            addends.append(input[j])
        elif test_sum > target_number:
            break
