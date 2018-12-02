import os

data = open("input.txt").read().split("\n")
data = [i for i in data if not i == '']

two_count = 0
three_count = 0

#import pdb;pdb.set_trace()
for name in data:
    seen_chars = set()
    two = False
    three = False

    for char in name:
        if char not in seen_chars:
            seen_chars.add(char)
            if name.count(char) == 2 and not two:
                two_count += 1
                two = True
            if name.count(char) == 3 and not three:
                three_count += 1
                three = True

print(two_count*three_count)
