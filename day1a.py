f = open("input.txt", "r")
dat = f.read().splitlines()

numAdd = 0
print(len(dat))

for i in range(1,len(dat)):
    if int(dat[i]) > int(dat[i-1]):
        numAdd += 1

print(numAdd)
