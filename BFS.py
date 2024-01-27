from collections import deque



def bfs(graph, start):
    visited = set() # Set to keep track of visited nodes
    queue = deque([start]) # Initialize a queue with the starting vertex

    while queue:
        vertex = queue.popleft() # Dequeue a vertex from the queue.
        if vertex not in visited:
            visited.add(vertex) # Mark it as visited
            print(vertex, end=" ") # Print the visited vertex


            # Add all of its neighbors that haven't been visited to the queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)




graph = {

    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


start_node = 'A'
bfs(graph, start_node)


# Breadth first search will expand all the neighbors of the starting node, and add all of their neighbors to the queue, before moving to the first neighbor of the starting
# node's first neighbor