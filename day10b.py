f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

m = {"]":"[", "}":"{", ">": "<", ")": "("}
p = {"[":2, "{":3, "<": 4, "(": 1}

pArr =  []
for line in dat:
    points = 0
    corrupt = False
    s = []
    
    for c in line:
        if c in "([{<":
            s.append(c)
        elif s[-1] != m[c]:
            corrupt = True
            break
        else:
            s.pop()

    if not corrupt:
        while s != []:
            points *= 5
            points += p[s.pop()]

        pArr.append(points)
    
pArr.sort()

print(pArr[len(pArr)//2])

