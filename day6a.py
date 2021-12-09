from collections import deque 

f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read()

doublingPeriod = 7
q = deque()

for num in dat.split(","):
    q.append(int(num))
q.append(None)

#print(q)

for i in range(80):
    node = q.popleft()
    
    while node is not None:
        #print(node)

        node -= 1
        if node < 0:
            q.append(8)
            q.append(6)
        else:
            q.append(node)
    
        node = q.popleft()

    q.append(None)
    #print()

print(len(q)-1)



