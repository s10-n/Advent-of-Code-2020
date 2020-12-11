import re

input_file = open('input')
adapters = []

for adapter in input_file:
    adapter = int(re.search('\d+',adapter).group())
    adapters.append(adapter)

adapters.sort()

joltage = 0
diff1 = 0
diff2 = 0
diff3 = 1

for adapter in adapters:
    if joltage+1 == adapter:
        joltage += 1
        diff1 +=1
    elif joltage+2 == adapter:
        joltage += 2
        diff2 +=1
    elif joltage+3 == adapter:
        joltage += 3
        diff3 +=1
        
print(diff1 * diff3)
