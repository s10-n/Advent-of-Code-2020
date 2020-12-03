import re,input

values = input.values

# add the letter positions to the parsable values list
range_values = re.findall("\d+",values)
parsable_values=[]
for i in range(0,len(range_values),2):
    parsable_values.append([int(range_values[i]),int(range_values[i+1])])

# add the target letters to the parsable values list
target_letters = re.findall("[a-z]{1}: ",values)
for i in range(len(target_letters)):
    parsable_values[i].append(re.sub(": ","",target_letters[i]))

# add the passwords to the parsable values list
passwords = re.findall(": [a-z]+",values)
for i in range(len(passwords)):
    parsable_values[i].append(re.sub(": ","",passwords[i]))

count = 0
for i in parsable_values: # check if the characters at one of the positions in the password are the given character
    if (i[3][i[0]-1] == i[2]) != (i[3][i[1]-1] == i[2]):
        count += 1
print(count)
