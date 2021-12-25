from copy import deepcopy

f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

dat = [list(d) for d in dat]

prev = deepcopy(dat)
m,n = len(dat), len(dat[0])
count = 1


def p(m):
    for r in m:
        print(r)
    print()

#p(dat)

while True:
    new = deepcopy(prev)

    moved = set()
    # move all east (left->right)
    for i in range(len(dat)):
        for j in range(len(dat[0])):
            if prev[i][j] == ">" and (i,j) not in moved:
                if prev[i][(j+1)%n] == ".":
                    new[i][(j+1)%n] = ">"
                    new[i][j] = "."
                    moved.add((i,(j+1)%n))
                    #print("dfas")

    ref = deepcopy(new)

    moved = set()
    # move all south (top->down)
    for i in range(len(dat)):
        for j in range(len(dat[0])):
            if ref[i][j] == "v" and (i,j) not in moved:
                if ref[(i+1)%m][j] == ".":
                    new[(i+1)%m][j] = "v"
                    new[i][j] = "."
                    moved.add(((i+1)%m, j))
                    #print("dfas")

    if prev == new:
        break

    prev = deepcopy(new)

    #print(count)
    #p(prev)
    #print()

    count += 1

print(count)






