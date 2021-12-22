#f = open("input.txt", "r")
f = open("testInput.txt", "r")
dat = f.read().splitlines()
nDat = []

for line in dat:
    switch, vals = line.split(" ")
    x,y,z = vals.split(",")
    sx,ex = [int(a) for a in x.split("=")[1].split("..")]
    sy,ey = [int(a) for a in y.split("=")[1].split("..")]
    sz,ez = [int(a) for a in z.split("=")[1].split("..")]

    #nDat.append((sx,ex,sy,ey,sz,ez))

    sx = max(-50, sx)
    sy = max(-50, sy)
    sz = max(-50, sz)

    ex = min(50, ex)
    ey = min(50, ey)
    ez = min(50, ez)
    
    for i in range(sx,ex+1):
        for j in range(sy,ey+1):
            for k in range(sz, ez+1):
                if switch == "on":
                    seen.add((i,j,k))
                else:
                    seen.discard((i,j,k))



print(len(seen))
