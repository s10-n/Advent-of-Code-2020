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
    number_of_people = len(group) # count the number of people who answered the survey
    group_answers = '' 
    for person in group:
        group_answers += person # add the person's answers to the group answer string
        for letter in group_answers:
            letter_count = group_answers.count(letter)
            if letter_count == number_of_people: # if the letter count in the group answers is the same as the number of people, they must have all answered that question
                sum += 1
                group_answers = re.sub(letter,'',group_answers)

print(sum)
