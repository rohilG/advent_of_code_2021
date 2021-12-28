from copy import deepcopy
f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

def valid(num,index):
    d = {'w':0,'x':0,'y':0,'z':0}

    for line in dat:
        l = line.split(" ")

        if len(l) == 2:
            d[l[1]] = num[index]
        
        elif l[0] == "add":
            d[l[1]] += d[l[2]] if l[2] in d else int(l[2])
        
        elif l[0] == "mul":
            d[l[1]] *= d[l[2]] if l[2] in d else int(l[2])
        
        elif l[0] == "div":
            if l[2].isnumeric():
                if l[2] == "0":
                    continue
            elif d[l[2]] == 0:
                continue

            d[l[1]] //= d[l[2]] if l[2] in d else int(l[2])
        
        elif l[0] == "mod" and d[l[1]] >= 0:
            if l[2].isnumeric():
                if int(l[2]) <= 0:
                    continue
            elif d[l[2]] <= 0:
                continue
            
            d[l[1]] %= d[l[2]] if l[2] in d else int(l[2])
        
        elif l[0] == "eql":
            b = d[l[2]] if l[2] in d else int(l[2])

            d[l[1]] = 1 if d[l[1]] == b else 0

    return d['z'] == 0

            
def works(num,index):
    if index >= 13:
        if valid(num,index):
            print(int("".join([str(x) for x in num])))
            exit(0) 
    else:

        for i in range(9,0,-1):
            num2 = num[::]
            num2[index] = i

            works(num2,index+1)

num = [9]*14
works(num[::], 0)
