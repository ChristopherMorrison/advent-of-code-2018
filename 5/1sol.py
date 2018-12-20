
# input data
data = open("input.txt").read()
data.strip()
alphabet = "abcdefghijklmnopqrstuvwxyz"

def react(data):
    # iterate until no changes are made on the condensing process
    changes_made = True
    while changes_made:
        changes_made = False
        data_size = len(data)
        for character in alphabet:
            form1 = character + character.upper()
            form2 = character.upper() + character
            data = data.replace(form1, "")
            data = data.replace(form2, "")
        if not data_size == len(data):
            changes_made = True
    return data
data = react(data)
print(data)
print(len(data)-1)

lows = set()
for character in alphabet:
    data2 = data.replace(character,"")
    data2 = data2.replace(character.upper(),"")
    lows.add(len(react(data2)))
    
print(min(lows)-1)