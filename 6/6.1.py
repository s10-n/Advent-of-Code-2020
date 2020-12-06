import re

file = open('input','r')
groups = []
current_group = []

for line in file:
    if line != '\n':
        line = re.sub('\n','',line) # remove the trailing newline from each person's response
        current_group.append(line) # add the person's answers to the group
    else:
        groups.append(current_group) # if the input is a newline, recognize this as the end of the group
        current_group = []

sum = 0
for group in groups:
    unique_letters = ''
    for person in group:
        for letter in person:
            if letter not in unique_letters: # check each person's answer to see if it's been said already
                unique_letters += letter
    sum += len(unique_letters) # add the number of unique letters from each group to the total

print(sum)       
