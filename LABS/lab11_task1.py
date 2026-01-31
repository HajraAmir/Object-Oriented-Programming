class GraphNode:
    def __init__(self, vertex=0, next_node=None):
        self.vertex = vertex
        self.next = next_node

class Graph:
    MAX = 10

    def __init__(self):
        self.headnodes = [None] * self.MAX
        self.n = 0
        self.visited = [False] * self.MAX

    def initialize_visited(self):
        self.visited = [False] * self.MAX

    def addVertex(self, vertex):
        if self.headnodes[vertex] is None:
            self.headnodes[vertex] = GraphNode(vertex)
            self.n += 1

    def removeVertex(self, vertex):
        if self.headnodes[vertex] is not None:
            for i in range(self.MAX):
                if self.headnodes[i] is not None:
                    self.removeEdge(i, vertex)
            self.headnodes[vertex] = None
            self.n -= 1

    def addEdge(self, vertex1, vertex2):
        if self.headnodes[vertex1] is not None and self.headnodes[vertex2] is not None:
            new_node = GraphNode(vertex2)
            new_node.next = self.headnodes[vertex1].next
            self.headnodes[vertex1].next = new_node

    def removeEdge(self, vertex1, vertex2):
        if self.headnodes[vertex1] is not None:
            curr = self.headnodes[vertex1]
            while curr.next is not None:
                if curr.next.vertex == vertex2:
                    curr.next = curr.next.next
                    break
                curr = curr.next

    def vertexExists(self, vertex):
        return self.headnodes[vertex] is not None

    def printGraph(self):
        for i in range(self.MAX):
            if self.headnodes[i] is not None:
                print(f"Vertex {i}:", end="")
                curr = self.headnodes[i].next
                while curr is not None:
                    print(f" {curr.vertex}", end=", ")
                    curr = curr.next
                print()

    def dfs(self, vertex):
        self.visited[vertex] = True
        print(vertex, end=" ")
        curr = self.headnodes[vertex].next
        while curr is not None:
            if not self.visited[curr.vertex]:
                self.dfs(curr.vertex)
            curr = curr.next

    def bfs(self, vertex):
        queue = []
        self.visited[vertex] = True
        queue.append(vertex)

        while queue:
            v = queue.pop(0)
            print(v, end=" ")
            curr = self.headnodes[v].next
            while curr is not None:
                if not self.visited[curr.vertex]:
                    self.visited[curr.vertex] = True
                    queue.append(curr.vertex)
                curr = curr.next


g = Graph()
for i in range(6):
    g.addVertex(i)
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 5)
g.addEdge(3, 4)
g.addEdge(4, 2)
g.addEdge(4, 5)
g.addEdge(5, 1)
g.printGraph()
print("DFS starting from vertex 0:")
g.dfs(0)
g.initialize_visited()
print("\nBFS starting from vertex 0:")
g.bfs(0)
