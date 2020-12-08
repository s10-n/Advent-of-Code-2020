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
checked_bags = []

def find_valid_bags(containing_bag,target_bag):
    global sum
    if rules[containing_bag]: # check if the bag has contents
        if target_bag in list(rules[containing_bag].keys()): # check if the target bag is in the current viewed bag
            if bag not in checked_bags: # make sure the parent bag hasn't been checked already
                sum += 1
                checked_bags.append(bag) # add the parent bag to the list of checked bags to ensure it's not double counted
        for i in list(rules[containing_bag].keys()): # do the same search on all child bags
            find_valid_bags(i,target_bag) 
            
for bag in rules:
    find_valid_bags(bag,'shiny gold')

print(sum)
