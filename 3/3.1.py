import input
mountain = input.values
height = len(mountain)
width = len(mountain[0])
x_position = 1
counter = 0
for i in range(1,height):
    x_position += 3
    if x_position > width:
        x_position -= width # wrap around to the other side if you exceed the width of the mountain
    if mountain[i][x_position-1] == '#':
        counter += 1
print(counter)
