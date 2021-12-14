f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()
poly = list(dat[0])
m = {}

for line in dat[2:]:
    l = line.split(" -> ")
    m[l[0]] = l[1]


cur = poly
for step in range(10):

    i = 0
    while i < len(cur)-1:
        if cur[i]+cur[i+1] in m:
            cur.insert(i+1, m[cur[i]+cur[i+1]])
            i += 2
        else:
            i += 1

from collections import Counter
ctr = Counter(cur)
print(ctr.most_common()[0][1] - ctr.most_common()[-1][1])

