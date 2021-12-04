from collections import Counter

f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

num = len(dat)

oxy = dat[::]
for i in range(len(dat[0])):
    if len(oxy) == 1:
        print(oxy[0])
        break

    ctr = Counter([r[i] for r in oxy]).most_common()
    if ctr[0][1] == ctr[1][1]:
        oxy = list(filter(lambda x: x[i] == "1", oxy))
    else:
        oxy = list(filter(lambda x: x[i] == ctr[0][0],oxy))

co2 = dat[::]
for i in range(len(dat[0])):
    if len(co2) == 1:
        print(co2[0])
        break

    ctr = Counter([r[i] for r in co2]).most_common()
    if ctr[0][1] == ctr[1][1]:
        co2 = list(filter(lambda x: x[i] == "0", co2))
    else:
        co2 = list(filter(lambda x: x[i] == ctr[-1][0], co2))

oxy = int(oxy[0], 2)
co2 = int(co2[0], 2)

print(oxy, co2, oxy*co2)

