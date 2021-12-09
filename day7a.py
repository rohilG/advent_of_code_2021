f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()
dat = sorted([int(d) for d in dat[0].split(",")])

median = None
if not len(dat) % 2:
    median = (dat[len(dat)//2] + dat[len(dat)//2 - 1]) // 2
else:
    median = dat[len(dat)//2]

print(median)
print(sum([abs(num-median) for num in dat]))

