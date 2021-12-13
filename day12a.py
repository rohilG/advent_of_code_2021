from collections import defaultdict

f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

adjList = defaultdict(list)

for line in dat:
    src,dst = line.split("-")

    if src == "start":
        adjList["start"].append(dst)
    elif dst == "start":
        adjList["start"].append(src)
    elif dst == "end":
        adjList[src].append("end")
    elif src == "end":
        adjList[dst].append("end")
    else:
        adjList[src].append(dst)
        adjList[dst].append(src)

# breadth first search from start
numRoutes = 0

#print(adjList)
#print()

def dfs(node, visited, curPath):
    global numRoutes
    
    #print(" "*d + node)
    
    # if found end path
    if node == "end":
        #print(curPath)
        numRoutes += 1
     
    # if visiting this small tunnel for the first time
    elif node.islower():
        #print("visiting this small tunnel for the first time")
        visited.add(node)
    
    # explore neighbours of this node
    for nei in adjList[node]:
        if nei not in visited:
            dfs(nei,visited, curPath+","+nei)
            visited.discard(nei)

dfs("start", set(), "start")
#print()
print(numRoutes)

