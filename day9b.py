from heapq import heappush, heappop

f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

totalRiskLevel = 0

heap = []

dat = [[int(n) for n in row] for row in dat]

def getBasinSize(i,j):
    global dat

    if i < 0 or i >= len(dat) or j < 0 or j >= len(dat[0]):
        return 0
    elif dat[i][j] == 9:
        return 0

    dat[i][j] = 9

    return 1 + getBasinSize(i-1,j) + getBasinSize(i+1,j) + getBasinSize(i,j-1) + getBasinSize(i, j+1)


for i in range(len(dat)):
    for j in range(len(dat[0])):
        if dat[i][j] != 9:
            basinSize = getBasinSize(i,j)
            heappush(heap, -basinSize)

a,b,c = heappop(heap), heappop(heap), heappop(heap)

print(a*b*-c)

