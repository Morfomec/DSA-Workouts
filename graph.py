# class Graph:

#     def __init__(self):
#         self.graph = {}

#     def add_vertex(self, v):
#         if v not in self.graph:
#             self.graph[v] = []

#     def add_edge(self, u, v):
#         self.add_vertex(u)
#         self.add_vertex(v)
#         self.graph[u].append(v)
#         self.graph[v].append(u)

#     def display(self):
#         for v in self.graph:
#             print(v, "->", self.graph[v])

# class Graph:

#     def __init__(self):
#         self.graph = {}

#     def add_vertex(self, u):
#         if u not in self.graph:
#             self.graph[u] = []
#         else:
#             print(u, "is already in the graph")


#     def add_edge(self, v1, v2):

#         self.add_vertex(v1)
#         self.add_vertex(v2)

#         if v1 not in self.graph[v2]:
#             self.graph[v2].append(v1)
#         if v2 not in self.graph[v1]:
#             self.graph[v1].append(v2)

# undirected , unweighted grap
# def add_edge(self, u, v):

#     if u == v:
#         return

#     self.add_vertex(u)
#     self.add_vertex(v)
#     if v not in self.graph[u]:
#         self.graph[u].append(v)
#     if u not in self.graph[v]:
#         self.graph[v].append(u)

# #undirected weighted graph
# def add_edge(self, u, v, w):

#     if u == v:
#         return

#     self.add_vertex(u)
#     self.add_vertex(v)

#     if u not in self.graph[v]:
#         self.graph[u][v] = w

#     if v not in self.graph[u]:
#         self.graph[v][u] = w

# def add_edge(self, u, v, w):

#     if u == v:
#         return

#     self.add_vertex(u)
#     self.add_vertex(v)

#     if u not in self.graph[v]:
#         self.graph[u][v] = w

#     if v not in self.graph[u]:
#         self.graph[v][u] = w

# def display(self):
#     for u in self.graph:
#         print(u, "-->", self.graph[u])

# def dfs(self, start):
#     visited = set()
#     self._dfs_helper(start, visited)

# def _dfs_helper(self, node, visited):
#     if node not in self.graph or not in visited:
#         return

#     visited.add(node)
#     print(node, end=" ")

#     for neighbor in self.graph[node]:
#         if neighbor not in visited:
#             self._dfs_helper(neighbor, visited)

# def dfs_stack(self, start):
#     if start not in self.graph:
#         return

#     visited = set()
#     stack = [start]

#     while stack:
#         node = stack.pop()

#         if node not in visited:
#             visited.add(node)
#             print(node, end=" ")

#             for neighbor in reversed(self.graph[node]):
#                 if neighbor not in visited:
#                     stack.append(neighbor)

# def dfs_stack(self, start):
#     if start not in self.graph:
#         return

#     visited = set()
#     stack = [start]

#     while stack:
#         popped = stack.pop()

#         if popped not in visited:
#             visited.add(popped)
#             print(popped, end=" ")

#             for neighbor in reversed(self.graph[popped]):
#                 if neighbor not in visited:
#                     stack.append(neighbor)
class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, u):
        if u not in self.graph:
            self.graph[u] = []
        else:
            print(u, "is already in the graph")

    def add_edge(self, v1, v2):

        self.add_vertex(v1)
        self.add_vertex(v2)

        if v1 not in self.graph[v2]:
            self.graph[v2].append(v1)
        if v2 not in self.graph[v1]:
            self.graph[v1].append(v2)

    def display(self):
        for u in self.graph:
            print(u, "-->", self.graph[u])


def BFS(node, graph, visited1):
    if node not in graph:
        print(node, "not present in the graph")
        return

    Queue = []
    Queue.append(node)
    visited1.add(node)

    while Queue:
        current = Queue.pop(0)
        print(current)
        for i in graph[current]:
            if i not in visited1:
                Queue.append(i)
                visited1.add(i)


def DFS(node, graph, visited):
    if node not in graph:
        print(node, "not present in graph")
        return

    stack = []
    stack.append(node)
    visited.add(node)

    while stack:
        current = stack.pop()
        print(current)
        for i in graph[current]:
            if i not in visited:
                stack.append(i)
                visited.add(i)


# visited1 = set()
# visited = set()

# g = Graph()

# g.add_edge(10, 11)
# g.add_edge(10, 11)
# g.add_edge(12, 11)
# g.add_edge(13, 10)

# g.display()

# print("BFS:")
# BFS(10, g.graph, visited1)

# print("DFS:")
# DFS(10, g.graph, visited)


class Graph:

    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, u):
        if u not in self.graph:
            self.graph[u] = []
        else:
            print(u, "already in the graph")
    
    def add_edge(self, u, v):

        self.add_vertex(u)
        self.add_vertex(v)

        if u not in self.graph[v]:
            self.graph[v].append(u)
        if v not in self.graph[u]:
            self.graph[u].append(v)

    def display(self):
        for u in self.graph:
            print(u, "-->", self.graph[u])


def BFS(node, graph, visited1):
    if node not in graph:
        print(node, "not present in the graph")
        return
    
    Queue = []
    Queue.append(node)
    visited1.add(node)

    while Queue:
        current = Queue.pop(0)
        print(current)
        for i in graph[current]:
            if i not in visited1:
                Queue.append(i)
                visited1.add(i)


def DFS(node, graph, visited):
    if node not in graph:
        print(node, "not present in the graph")
        return
    
    stack = []
    stack.append(node)
    visited.add(node)

    while stack:
        current = stack.pop()
        print(current)
        for i in graph[current]:
            if i not in visited:
                stack.append(i)
                visited.add(i)


visited1 = set()
visited = set()

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(3, 7)
g.display()
BFS(1, g.graph, visited1)
DFS(11, g.graph, visited1)



class Graph:

    def __init__(self):
        self.graph = {}


    def add_vertex(self, u):

        if u not in self.graph:
            self.graph[u] = []
        else:
            print(u, "already present in the graph")

    def add_edge(self, u, v):

        self.add_vertex(u)
        self.add_vertex(v)

        if u not in self.graph[v]:
            self.graph[v].append(u)
        if v not in self.graph[u]:
            self.graph[u].append(v)

    def display(self):
        for u in self.graph:
            print(u, "-->", self.graph[u])


def BFS(node, graph, visited):

    if node not in graph:
        print("Node not present")
        return 

    Queue = []
    Queue.append(node)
    visited.add(node)

    while Queue:
        current = Queue.pop(0)
        print(current)

        for i in graph[current]:
            if i not in visited:
                Queue.append(i)
                visited.add(i)

def DFS(node, graph, visited1):

    if node not in graph:
        print("Node not present")
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

visited = set()
visited1 = set()


