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

def dfs(node, visited, curPath, doubleSmallCave, d):
    global numRoutes
    
    #print(" "*d + node)
    
    # if found end path
    if node == "end":
        if doubleSmallCave == "start" or visited[doubleSmallCave] == 2:
            numRoutes += 1
     
    # if visiting this small tunnel for the first time
    elif node.islower():
        '''
        if visited[node] == 0:
            print("visiting this small tunnel for the first time", node)
        elif visited[node] == 1:
            print("visiting this small tunnel for the second time", node)
        else:
            print("MAJOR ISSUE", visited[node])
        '''

        visited[node] += 1
    
    # explore neighbours of this node
    for nei in adjList[node]:
        if nei == doubleSmallCave:
            if visited[nei] < 2:
                dfs(nei,visited, curPath+","+nei, doubleSmallCave, d+1)
                if nei in visited:
                    visited[nei] -= 1

        elif nei not in visited or visited[nei] == 0:
            dfs(nei,visited, curPath+","+nei, doubleSmallCave, d+1)
            if nei in visited:
                visited[nei] -= 1

for k in list(adjList.keys())[::]:
    if k.islower():
        #print("special cave:", k)
        dfs("start", defaultdict(int), "start", k, 0)
        #print()
        
#print()
print(numRoutes)

