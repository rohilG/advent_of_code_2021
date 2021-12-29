#f = open("input.txt", "r")
f = open("testInput.txt", "r")

dat = f.read().splitlines()
a,b = dat[0].split(", ")

endY = [int(x) for x in b.split("=")[1].split("..")]
endX = [int(x) for x in a.split(": ")[1].split("=")[1].split("..")]

assert(endY[0] <= endY[1])
assert(endX[0] <= endX[1])

def isPossible(x,y):
    

for x in range(endX[0], endX[1]+1):
    for y in range(endY[0], endY[1]+1):
        # proceed backwards
        if isPossible(x,y):
            print(x,y)
            break



