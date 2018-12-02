data = open("input.txt").read().split("\n")
ints = [int(i) for i in data if not i == ""]
print(sum(ints))


