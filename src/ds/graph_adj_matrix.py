class Vertex:

    def __init__(self, name):
        self.name = name


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

        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end='')

            for j in range(len(self.edges)):
                print(self.edges[i][j], end=' ')

            print(' ')


if __name__ == '__main__':

    g = Graph()
    a = Vertex('A')
    g.add_vertex(a)
    g.add_vertex(Vertex('B'))

    for i in range(ord('A'), ord('K')):
        g.add_vertex(Vertex(chr(i)))

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FJ', 'GJ', 'FH']

    for edge in edges:
        g.add_edge(edge[0], edge[1])

    g.print_graph()
