f = open("input.txt", "r")
dat = f.read().splitlines()

x,y,aim = 0,0,0

for command in dat:
    course, val = command.split(" ")
    val = int(val)
    if course == "forward":
       x += val
       y += aim*val
    elif course == "down":
        aim += val
    elif course == "up":
        aim -= val

print(x,y,x*y)
