from collections import Counter

f = open("input.txt", "r")
#$f = open("testInput.txt", "r")
dat = f.read().splitlines()

seen = {}
numOverTwo = 0

for line in dat:
    s,e = line.split(" -> ")
    x1,y1 = [int(n) for n in s.split(",")]
    x2,y2 = [int(n) for n in e.split(",")]

    #print(str(x1)+","+str(y1)+" "+str(x2)+","+str(y2))

    if x1 == x2:
        while y1 != y2:
            if (x1,y1) not in seen:
                seen[(x1,y1)] = 1
            else:
                seen[(x1,y1)] += 1
            
            if y1 < y2:
                y1 += 1
            else:
                y1 -= 1
            
            #print(str(x1)+","+str(y1)+" "+str(x2)+","+str(y2))
        
        if (x1,y1) not in seen:
            seen[(x1,y1)] = 1
        else:
            seen[(x1,y1)] += 1
    
    elif y1 == y2:
        while x1 != x2:
            if (x1,y1) not in seen:
                seen[(x1,y1)] = 1
            else:
                seen[(x1,y1)] += 1
            
            if x1 < x2:
                x1 += 1
            else:
                x1 -= 1
            
            #print(str(x1)+","+str(y1)+" "+str(x2)+","+str(y2))
        
        if (x1,y1) not in seen:
            seen[(x1,y1)] = 1
        else:
            seen[(x1,y1)] += 1

    #print()

for k in seen.keys():
    if seen[k] > 1:
        numOverTwo += 1

#print(seen)
print(numOverTwo)



