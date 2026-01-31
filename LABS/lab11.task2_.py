def directed_graph(num_vertices, edges):
    adj_list = [[] for i in range(num_vertices)]
    for i, j in edges:
        adj_list[i].append(j) 
    return adj_list

def print_graph(adj_list):
    for i in range(len(adj_list)):
        if adj_list[i]:
            print(f"{i} ->", end=" ")
            for neighbor in adj_list[i]:
                print(neighbor, end=" ")
            print()  
        else:
            print(f"{i} -> x")
num_vertices = 8
edges = [
    (0, 3), (1, 5), (1, 6), (2, 5), (4, 2),
    (4, 6), (4, 7), (5, 6), (5, 7), (6, 5), 
    (7, 5)
]

graph = directed_graph(num_vertices, edges)
print_graph(graph)
