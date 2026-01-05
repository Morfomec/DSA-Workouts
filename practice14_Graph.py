class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, u):
        if not self.graph:
            self.graph[u] = []
            return 

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)

        if v not in self.graph[u]:
            self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].append(u)
    
    def display(self):
        for u in self.graph:
            print(u, "-->", self.graph[u])

def BFS(node, graph, visited):

    if node not in graph:
        print("Graph not present")
        return
    
    queue = []
    queue.append(node)
    visited.add(node)

    while queue:
        current = queue.pop(0)
        print(current)

        for i in graph[current]:
            if i not in visited:
                queue.append(i)
                visited.add(i)

def DFS(node, graph, visited):
    if node not in graph:
        return

    stack = []
    stack.append(node)
    visited1.add(node)

    while stack:
        current = stack.pop()
        print(current)

        for i in graph[current]:
            if i not in visited1:
                stack.append(i)
                visited1.add(i)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()
visited1 = set()
BFS('A', graph, visited)
print()
DFS("A", graph, visited1)