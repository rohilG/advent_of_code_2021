from collections import Counter

f = open("input.txt", "r")
dat = f.read().splitlines()

gamma = int("".join([Counter([r[i] for r in dat]).most_common(1)[0][0] for i in range(len(dat[0]))]), 2)

epsilon = int("".join([Counter([r[i] for r in dat]).most_common()[-1][0] for i in range(len(dat[0]))]), 2)

print(gamma, epsilon, gamma * epsilon)
