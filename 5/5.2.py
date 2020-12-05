boarding_passes_file = open('input','r')
boarding_passes = []

# write each line in the input file into a list of boarding passes
for line in boarding_passes_file:
    boarding_passes.append(line[:-1])

seat_ids = [] # create an empty list of seat IDs

for boarding_pass in boarding_passes:
    # reset possible seats
    row_range,column_range = [],[]
    for row in range(128): row_range.append(row) # create 128 possible rows
    for column in range(8): column_range.append(row) # create 8 possible columns
   
    for letter in boarding_pass[:-3]: # use the first seven letters to determine the row
        rows = int(len(row_range) / 2) 
        if letter == 'F':
            row_range = row_range[:rows] # look in the first half
        elif letter == 'B':
            row_range = row_range[rows:] # look in the second half
        row = row_range[0]

    for letter in boarding_pass[-3:]: # use the last three letters to determine the column
        columns = int(len(column_range) / 2)
        if letter == 'L':
            column_range = column_range[:columns] # look in the first half
        elif letter == 'R':
            column_range = column_range[columns:] # look in the second half
        column = column_range[0]

    seat_ids.append(row * 8 + column) # add the seat ID to the list

seat_ids.sort()
counter = seat_ids[0] # start the counter with the first seat ID to ignore any missing seats at the beginning
for i in seat_ids:
    if initial_value != i: # figure out where the seats don't jive with the counter
        print(f'{initial_value} is your seat.')
        break
    initial_value += 1
