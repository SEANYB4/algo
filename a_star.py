import heapq

class Node:
    def __init__(self, name, heuristic=0):
        self.name = name
        self.heuristic = heuristic
        self.adjacents = []
        self.parent = None
        self.g = float('inf') # Cost to reach this node from the start node
        self.f = float('inf') # Total cost (g + heuristic)

    def __lt__(self, other):
        return self.f < other.f
    
    def add_adjacent(self, node, cost):
        self.adjacents.append((node, cost))



def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (start.f, start))
    start.g = 0
    start.f = start.g + start.heuristic

    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == goal:
            return reconstruct_path(current)        

        for neighbor, cost in current.adjacents:
            tentative_g_score = current.g + cost
            if tentative_g_score < neighbor.g:
                neighbor.parent = current
                neighbor.g = tentative_g_score
                neighbor.f = tentative_g_score + neighbor.heuristic
                if neighbor not in open_set:
                    heapq.heappush(open_set, (neighbor.f, neighbor))

    return None


def reconstruct_path(current):
    path = []
    while current:
        path.append(current.name)
        current = current.parent
    return path[::-1]




node_A = Node('A', heuristic=10)
node_B = Node('B', heuristic=8)
node_C = Node('C', heuristic=5)
node_D = Node('D', heuristic=7)
node_E = Node('E', heuristic=3)
node_G = Node('G', heuristic=0) # Goal


# Create graph with edges (adjacent nodes and their costs)

node_A.add_adjacent(node_B, cost=1)
node_A.add_adjacent(node_C, cost=3)
node_B.add_adjacent(node_C, cost=1)
node_B.add_adjacent(node_D, cost=5)
node_C.add_adjacent(node_D, cost=3)
node_C.add_adjacent(node_E, cost=1)
node_D.add_adjacent(node_G, cost=2)
node_E.add_adjacent(node_G, cost=4)


# Perform A* search

path = a_star(node_A, node_G)

if path:
    print(f"Path found by A*: {path}")

