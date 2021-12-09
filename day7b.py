from math import ceil,floor

f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()
dat = [int(d) for d in dat[0].split(",")]

avg = sum(dat)/len(dat)

a = [(abs(num-ceil(avg))) for num in dat]
b = [(abs(num-floor(avg))) for num in dat]

print(sum([num*(num+1)//2 for num in a]))
print(sum([num*(num+1)//2 for num in b]))


