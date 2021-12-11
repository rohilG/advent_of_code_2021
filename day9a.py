f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

totalRiskLevel = 0

dat = [[int(n) for n in row] for row in dat]

def lower(i,j):
    if i-1 >= 0 and dat[i-1][j] <= dat[i][j]:
        return False
    
    if i+1 < len(dat) and dat[i+1][j] <= dat[i][j]:
        return False

    if j-1 >= 0 and dat[i][j-1] <= dat[i][j]:
        return False

    if j+1 < len(dat[0]) and dat[i][j+1] <= dat[i][j]:
        return False

    return True

for i in range(len(dat)):
    for j in range(len(dat[0])):
        if lower(i,j):
            totalRiskLevel += (dat[i][j] + 1)

print(totalRiskLevel)

