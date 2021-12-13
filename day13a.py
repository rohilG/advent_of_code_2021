from collections import defaultdict
f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

dots = []

for line in dat:
    a = line.split(",")

    if a[0] and len(a) == 1:
        line = line.split(" ")
        print(line)
        c,num = line[-1].split("=")
        num = int(num)

        for i in range(len(dots)):
            x,y = dots[i]
            if c == 'x':
                if x > num:
                    dots[i][0] = num - (x-num)
            elif c== 'y':
                if y > num:
                    dots[i][1] = num - (y-num)
        break
    elif len(a) == 2:
        dots.append(a)
    else:
        dots = [[int(a),int(b)] for a,b in dots]

dots.sort()
dots = [(int(a),int(b)) for a,b in dots]
print(dots)
print(len(set(dots)))


