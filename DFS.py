def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ") # Process the node (for example, just print it)

    for next_node in graph[start]:
        if next_node not in visited:
            dfs(graph, next_node, visited)
    return visited



graph = {

    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']

}

start_node = 'A'
dfs(graph, start_node)