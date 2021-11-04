# implementation of an undirected graph using Adjacency Matrix, with weighted or unweighted edges
class Vertex:
    def __init__(self, n):
        self.name = n


class Graph:
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        print('   ' + '  '.join(self.edge_indices.keys()))
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end='')
            print(str(self.edges[i]))
        # for j in range(len(self.edges)):
        # 	print(self.edges[i][j], end=' ')
        # print('')


g = Graph()
# print(str(len(g.vertices)))

# a = Vertex('A')
# g.add_vertex(a)
# g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('G')):
    g.add_vertex(Vertex(chr(i)))

# edges = ['AF', 'AC', 'AB', 'FE', 'FC', 'CD', 'BC', 'BD', 'ED']

edgesDict = {
    'AF': 14,
    'AC': 9,
    'AB': 7,
    'FE': 9,
    'FC': 2,
    'CD': 11,
    'BC': 10,
    'BD': 15,
    'ED': 6
}

for key, value in edgesDict.items():
    g.add_edge(key[:1], key[1:], value)

# for edge in edges:
#     g.add_edge(edge[:1], edge[1:])

g.print_graph()
