f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = [int(d) for d in f.read().split(",")]

doublingPeriod = 7

a = [dat.count(i) for i in range(9)]

for i in range(256):
    cur = a.pop(0)
    a[6] += cur
    a.append(cur)
    assert(len(a) == 9)

print(sum(a))

