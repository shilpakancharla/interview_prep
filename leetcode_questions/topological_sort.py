from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list) # Dictionary with adjacency list
        self.v = vertices # Number of vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        # Mark current node as visited
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_util(i,  visited, stack)

        stack.insert(0, v) # Insert at top of stack

    def topological_sort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.v
        stack = []

        # Call recursive helper function to store topological sort
        for i in range(self.v):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)

        print(stack)

# Driver code
g = Graph(5)
g.add_edge(4, 1)
g.add_edge(2, 5)
g.add_edge(4, 2)
g.add_edge(1, 5)
g.add_edge(3, 4)

g.topological_sort()
