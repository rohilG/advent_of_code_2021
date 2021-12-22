f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

# mat[i][j] == lowest risk value to get to dat[i][j]
mat= [[0 for _ in len(dat[0])] for _ in len(dat)]

def explore(i,j):
    if i < 0 or i >= len(dat) or j < 0 or j >= len(dat[0]):
        return


