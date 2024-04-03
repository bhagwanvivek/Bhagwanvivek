class Graph:
    def __init__(self):
        self.graph={}
    def add_edge(self,node,neighbor):
        self.graph.setdefault(node,[].append(neighbor))
def depth_first_search(graph,start,visited=set()):
    visited.add(start)
    print(start,end='')
    for neighbor in graph.get(start,[]):
        if neighbor not in visited:
            depth_first_search(graph,neighbor,visited)
g=Graph()
g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','D')
g.add_edge('B','E')
g.add_edge('E','F')
print("DFS sTARTING FROM A:")
depth_first_search(g.graph,'A')
