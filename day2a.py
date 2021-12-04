f = open("input.txt", "r")
dat = f.read().splitlines()

x,y = 0,0

for command in dat:
    course, val = command.split(" ")
    val = int(val)
    if course == "forward":
        x += val
    elif course == "down":
        y += val
    elif course == "up":
        y -= val

print(x,y,x*y)
