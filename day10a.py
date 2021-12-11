f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

s = []
m = {"]":"[", "}":"{", '>': '<', ")": "("}
p = {"]":57, "}":1197, '>': 25137, ")": 3}

points = 0
for line in dat:
    for c in line:
        if c in "([{<":
            s.append(c)
        elif s[-1] != m[c]:
            points += p[c]
            break
        else:
            s.pop()
    

print(points)

