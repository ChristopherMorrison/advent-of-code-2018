data = open("1input.txt").read().split("\n")
data = [int(i) for i in data if not i == '']
#data = set(data)
seen = {0}
val = 0
while 1:
    for i in data:
        val = val + i
        if val in seen:
            print(">"+str(val))
            quit(0)
        seen.add(val)
