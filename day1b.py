f = open("input.txt", "r")
dat = [int(x) for x in f.read().splitlines()]

numAdd = 0
prevTrip = sum(dat[:3])

for i in range(1, len(dat)):
    curTrip = sum(dat[i:i+3])
    if curTrip > prevTrip:
        numAdd += 1
    prevTrip = curTrip

print(numAdd)
