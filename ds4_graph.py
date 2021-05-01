class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    # Get the keys of the dictionary
    def get_vertices(self):
        return list(self.gdict.keys())

    def edges(self):
        return self.find_edges()

    # Find the distinct list of edges
    def find_edges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

    # Add the vertex as a key
    def add_vertex(self, vrtx):
       if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    # Add the new edge
    def add_edge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]


if __name__ == "__main__":

    # Create the dictionary with graph elements
    graph = { "a" : ["b","c"],
              "b" : ["a", "d"],
              "c" : ["a", "d"],
              "d" : ["e"],
              "e" : ["d"]
             }

    # Print the graph
    print(f"Graph -> {graph}")
    # {'c': ['a', 'd'], 'a': ['b', 'c'], 'e': ['d'], 'd': ['e'], 'b': ['a', 'd']}

    g = Graph(graph)

    print(f"Vertices -> {g.get_vertices()}")
    # ['d', 'b', 'e', 'c', 'a']

    print(f"Edges -> {g.edges()}")
    # [{'b', 'a'}, {'b', 'd'}, {'e', 'd'}, {'a', 'c'}, {'c', 'd'}]

    g.add_vertex("f")
    print(f"Vertices (2) -> {g.get_vertices()}")
    # ['f', 'e', 'b', 'a', 'c','d']

    g.add_edge({'a', 'e'})
    g.add_edge({'a', 'c'})
    print(f"Edges(2) -> {g.edges()}")
    # [{'e', 'd'}, {'b', 'a'}, {'b', 'd'}, {'a', 'c'}, {'a', 'e'}, {'c', 'd'}]