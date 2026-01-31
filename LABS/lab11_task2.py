def undirected_graph(num_vertices, edges):
   
    adj_list = [[] for i in range(num_vertices)]
    for i, j in edges:
        adj_list[i].append(j)
        adj_list[j].append(i)
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
num_vertices = 9
edges = [
    (2, 0), (0, 3), (5, 2), (4, 6), (4, 0),
    (1, 3), (2, 1), (6, 1)
]

graph = undirected_graph(num_vertices, edges)
print_graph(graph)
