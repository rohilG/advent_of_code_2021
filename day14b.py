from collections import defaultdict, Counter
from copy import deepcopy

f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()
poly = list(dat[0])
m = {}

for line in dat[2:]:
    l = line.split(" -> ")
    m[l[0]] = l[1]

pairs = defaultdict(int)
def dictify(s, d):
    for i in range(len(s)-1):
        d[s[i]+s[i+1]] += 1 

dictify(poly,pairs)

c = "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
d = defaultdict(int)
dictify(c,d)

'''
c = "NCNBCHB" 
d = defaultdict(int)
dictify(c,d)


c = "NBCCNBBBCBHCB" 
d = defaultdict(int)
dictify(c,d)
'''

#print(m)

last= pairs
cur = deepcopy(pairs)
for step in range(40):
    #print(last)

    for k in list(last.keys()):
        if k in m:
            #print(k)
            # when do we delete m[k]? How do we know it doesn't exist anymore? Well.. was it created?
            # created if in cur but not in old

            cur[k[0] + m[k]] += last[k]
            cur[m[k] + k[1]] += last[k]
            #print(last)
            cur[k] -= last[k]
            if cur[k] == 0:
                del cur[k]
            #print(cur)
    
    last = deepcopy(cur)
    #print(step+1, sum(v for v in cur.values()))


letters = defaultdict(int)
for k,v in cur.items():
    letters[k[0]] += v
    letters[k[1]] += v


a = sorted(v for v in letters.values())
if a[-1]%2:
    a[-1] += 1
if a[0] %2:
    a[0] += 1

print(a[-1]//2-a[0]//2)


#print('cur',cur)
#print('right', d)
#assert(cur == d)


