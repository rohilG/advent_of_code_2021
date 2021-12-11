f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

numFlashes = 0
dat = [[int(num) for num in row] for row in dat]

def printDat():
    for row in dat:
        print("".join([str(num) for num in row]))

def checkRow(i,j, sameRow = False):
    global dat

    if j -1 >= 0:
        if dat[i][j-1] == 9:
            flash(i,j-1)
        elif dat[i][j-1] != 0:
            dat[i][j-1] += 1
    
    if not sameRow:
        if dat[i][j] == 9:
            flash(i,j)
        elif dat[i][j] != 0:
            dat[i][j] += 1

    if j +1 < len(dat[0]):
        if dat[i][j+1] == 9:
            flash(i,j+1)
        elif dat[i][j+1] != 0:
            dat[i][j+1] += 1

def flash(i,j):
    global numFlashes, dat, flashed

    if (i,j) in flashed:
        return
    flashed.add((i,j))

    numFlashes += 1

    if i -1 >= 0:
        checkRow(i-1,j)
    
    checkRow(i,j,True)
    
    if i +1 < len(dat):
        checkRow(i+1,j)

    dat[i][j] = 0


def allZero():
    for row in dat:
        if sum(row) != 0:
            return False

    return True

#print("Before any steps:")
#printDat()

for step in range(1,2000):
    flashed = set()

    for i in range(len(dat)):
        for j in range(len(dat[0])):
            dat[i][j] += 1
    
    for i in range(len(dat)):
        for j in range(len(dat[0])):
            if dat[i][j] > 9:
                flash(i,j)

    if allZero():
        print(step)
        break

    #print()
    #print("After step " + str(step) + ":")
    #printDat()
                
#print(numFlashes)



