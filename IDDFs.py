# graph = {
#     '5': ['3', '7'],
#     '3': ['2', '4'],
#     '7': ['8'],
#     '2': [],
#     '4': ['8'],
#     '8': []
# }

# def dfs_limited(graph, node, depth, visited):
#     if depth >= 0:
#         print(node, end=" ")
#         visited.add(node)
#         if depth == 0:
#             return
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 dfs_limited(graph, neighbor, depth - 1, visited)

# def iddfs(graph, start_node, max_depth):
#     for depth in range(max_depth + 1):
#         visited = set()
#         print(f"\n {depth}: ", end="")
#         dfs_limited(graph, start_node, depth, visited)

# print("IDDFS Traversal is:-")
# iddfs(graph, '5', 3)
#====Bidirectional Search========

 

