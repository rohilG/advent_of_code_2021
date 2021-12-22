f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

enchancement = dat[0]
old = dat[2:]

def esketit(old, num):
    mat = [['.' for _ in range(len(old[0]))] for _ in range(len(old))]
    out = [['.' for _ in range(len(old[0]))] for _ in range(len(old))]

    #print(len(mat), len(mat[0]))
    #print(len(old), len(old[0]))

    for i in range(len(old)):
        for j in range(len(old[0])):
            mat[i][j] = old[i][j]

            #try:
                #print('old',old[i][j])
                #print('mat',mat[i+2][j+2])
                #mat[i+2][j+2] = old[i][j]
            #except:
                #print(i,j)
                #print(old[i][j])
                #return -1
                #print('old',old[i][j], end= " ")
                #print('mat',mat[i][j])

                #print()

    for i in range(len(mat)-2):
        for j in range(len(mat[0])-2):
            # get cube
            cur = mat[i][j:j+3]
            cur += mat[i+1][j:j+3]
            cur += mat[i+2][j:j+3]

            assert(len(cur) == 9)

            cur = int("".join(["1" if c == "#" else "0" for c in cur]), 2)

            # first time
            if cur == 0 and num == 0:
                out[i+1][j+1] = "."
            else:
                out[i+1][j+1] = enchancement[cur]

    return out

def printIt(out):
    for r in out:
        print(r)

    print()
    print()

#augment it
for i in range(len(old)):
    old[i] = ".." + old[i] + ".."

old.insert(0, "".join(['.' for _ in range(len(old[0]))]))
old.insert(0, "".join(['.' for _ in range(len(old[0]))]))
#old.insert(0, "".join(['.' for _ in range(len(old[0]))]))
#old.append("".join(['.' for _ in range(len(old[0]))]))
old.append("".join(['.' for _ in range(len(old[0]))]))
old.append("".join(['.' for _ in range(len(old[0]))]))

printIt(old)
out = esketit(old,0)
printIt(out)
out2 = esketit(out,1)
printIt(out2)

print(sum([r.count("#") for r in out2]))

