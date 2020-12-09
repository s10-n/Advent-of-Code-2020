input_file = open('input','r')
input = input_file.read()

import re
program = []
instructions = re.findall('[a-z]{3}',input)
arguments = re.findall('-*\d+',input)
for i in range(len(instructions)):
    program.append([instructions[i],int(arguments[i])])

def evaluate_instruction(index, accumulator, viewed_indices):
    instruction = program[index][0]
    argument = program[index][1]
    if index not in viewed_indices:
        viewed_indices.append(index)
        if instruction == 'acc':
            accumulator += argument
            evaluate_instruction(index + 1, accumulator, viewed_indices)
        elif instruction == 'jmp':
            evaluate_instruction(index + argument, accumulator, viewed_indices)
        elif instruction == 'nop':
            evaluate_instruction(index + 1, accumulator, viewed_indices)
    else:
        print(accumulator)
    
evaluate_instruction(0, 0, [])
