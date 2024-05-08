graph={
     5: [3, 7],
    3: [2, 4],
    7: [8],
    2: [],
    4: [8],
    8: []
}

visitedSet=set()
visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neighboor in graph.get(m,[]):
            if neighboor not in visited:
                visited.append(neighboor)
                queue.append(neighboor)

bfs(visited,graph,5)

def dfs(visitedSet,graph,node):
    if node not in visitedSet:
        print(node,end=" ")
        visitedSet.add(node)
        for neighboor in graph[node]:
            dfs(visitedSet,graph,neighboor)
print(" ")
print("The DFS is - ")
dfs(visitedSet,graph,5)