import os
import re

# read in
data = [line for line in open("input.txt").read().split("\n") if not line == '']

# convert to regex objects so we can easily use the data
expression = r"#(.*) @ (.*),(.*): (.*)x(.*)"
data = [re.match(expression,line) for line in data]
i_number = 1
i_x_pos = 2
i_y_pos = 3
i_x_dim = 4
i_y_dim = 5

# Create a map of for the max possible size of our data
# max size is max(index+dimesion)
max_x = int(max([item.group(i_x_pos)+item.group(i_x_dim) for item in data]))
max_y = int(max([item.group(i_y_pos)+item.group(i_y_dim)for item in data]))

# this is a dumb way to do this but it works
unique_points = set()
shared_points = set()

for square in data:
    for y in range(int(square.group(i_y_dim))):
        for x in range(int(square.group(i_x_dim))):
            point = str(int(square.group(i_y_pos))+y) + ":" + str(int(square.group(i_x_pos))+x)
            if not point in unique_points:
                unique_points.add(point)
            elif point not in shared_points:
                shared_points.add(point)

print("Overlapping fabric units="+str(len(shared_points)))

# part 2 find the square that doesn't overlap with any other square
for square in data:
    overlaps = False
    for y in range(int(square.group(i_y_dim))):
        for x in range(int(square.group(i_x_dim))):
            point = str(int(square.group(i_y_pos))+y) + ":" + str(int(square.group(i_x_pos))+x)
            if point in shared_points:
                overlaps = True
    if not overlaps:
        print("Section ID that does not overlap="+square.group(i_number))
