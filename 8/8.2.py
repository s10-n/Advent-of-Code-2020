input_file = open('input','r')
input = input_file.read()

import re
program = []
instructions = re.findall('[a-z]{3}',input)
arguments = re.findall('-*\d+',input)
for i in range(len(instructions)):
    program.append([instructions[i],int(arguments[i])])

def evaluate_instruction(index, accumulator, visited_indices):
    if index == len(program) - 1:
        print('Program finished successfully. Accumulator value: ' + str(accumulator))
        return True
    else:
        instruction = program[index][0]
        argument = program[index][1]
        if index not in visited_indices:
            visited_indices.append(index)
            if instruction == 'acc':
                accumulator += argument
                evaluate_instruction(index + 1, accumulator, visited_indices)
            elif instruction == 'jmp':
                evaluate_instruction(index + argument, accumulator,visited_indices)
            elif instruction == 'nop':
                evaluate_instruction(index + 1, accumulator, visited_indices)
        else:
            return False
    
for i in range(len(program)):
    if program[i][0] == 'jmp':
        program[i][0] = 'nop'
    elif program[i][0] == 'nop':
        program[i][0] = 'jmp'
    if not evaluate_instruction(0, 0,[]):
            if program[i][0] == 'jmp':
                program[i][0] = 'nop'
            elif program[i][0] == 'nop':
                program[i][0] = 'jmp'
