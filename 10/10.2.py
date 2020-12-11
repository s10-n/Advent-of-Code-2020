import re

input_file = open('input')
adapters = []

adapters.append(0)
for adapter in input_file:
    adapter = int(re.search('\d+',adapter).group())
    adapters.append(adapter)
adapters.sort()
adapters.append(adapters[-1] + 3)

adapter_groups = []
for i in range(len(adapters)):
    adapter_groups.append([])
               
adapter_groups_index = 0
last_joltage = 0

for adapter in adapters:
    if adapter - last_joltage >= 3:
        adapter_groups_index += 1
    adapter_groups[adapter_groups_index].append(adapter)
    last_joltage = adapter

adapter_possibilities = []

for adapter_group in adapter_groups:
    length = len(adapter_group)
    if length == 1 or length == 2:
        adapter_possibilities.append(1)
    if length == 3:
        adapter_possibilities.append(2)
    if length == 4:
        adapter_possibilities.append(4)
    if length == 5:
        adapter_possibilities.append(7)

product = 1
for i in adapter_possibilities:
    product *= i

print(product)
