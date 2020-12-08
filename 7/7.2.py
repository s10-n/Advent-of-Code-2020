import re

rules = {}

# convert the text input into a dictionary, with bags as keys and their contents as values
input = open('input')
for line in input:
    line = re.sub('\n','',line)
    containing_bag = re.search('\w+ \w+',line).group(0)
    rules[containing_bag] = {}
    contained_bags = re.findall('\d \w+ \w+',line)
    for bag in contained_bags:
        quantity = re.search('\d',bag).group(0)
        colour = re.search('[a-z]+ \w+',bag).group(0)
        rules[containing_bag][colour] = int(quantity)

sum = 0

def find_total_bags(containing_bag, multiplier):
    global sum
    for contained_bag in rules[containing_bag].keys(): # check all of the bags in the current bag
        sum += rules[containing_bag][contained_bag] * multiplier # the total number of bags is the number plus the multiplier
        find_total_bags(contained_bag, rules[containing_bag][contained_bag] * multiplier) # do the same check on all child bags, increasing the multiplier by the number of bags

find_total_bags('shiny gold',1)

print(sum)
