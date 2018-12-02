data = open("input.txt").read().split("\n")
data = [i for i in data if not i == '']
#data = set(data)

for index in range(len(data)-1):
    name = data[index]
    for other_name in data[index+1:]:
        diff_count = 0
        for char_index in range(len(name)):
            if not name[char_index] == other_name[char_index]:
                diff_count+=1
        if diff_count == 1:
            print("["+str(data.index(name))       +"]\t"+name)
            print("["+str(data.index(other_name)) +"]\t"+other_name)
            quit(0)
    
