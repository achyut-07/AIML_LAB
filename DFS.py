graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}
visited=set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for n in graph[node]:
            dfs(visited,graph,n)

print("DFS Traversal is:- ")
dfs(visited,graph,'5')