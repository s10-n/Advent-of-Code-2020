import input
mountain = input.values
height = len(mountain)
width = len(mountain[0])
x_position = 1
counter = 0

def slope(right_increment,down_increment):
    x_position = 1
    counter = 0
    for i in range(1,height,down_increment):
        x_position += right_increment
        if x_position > width:
            x_position -= width # wrap around to the other side if you exceed the width of the mountain
        if mountain[i][x_position-1] == '#':
            counter += 1
    return(counter)

print(slope(1,1) * slope(3,1) * slope(5,1) * slope(7,1) * slope(1,2))
