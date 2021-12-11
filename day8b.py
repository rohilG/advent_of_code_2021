f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

digit = {2:[1], 3:[7], 4:[4], 5:[2,3,5], 6:[0,6,9], 7:[8]}
uniqueDigits = {2,3,4,7}

unique = 0

for line in dat:
    a,b = line.split(" | ")
    b = b.split(" ")
    for char in b:
        word = len(set(list(char)))

        if word in uniqueDigits:
            unique += 1
    
print(unique)


