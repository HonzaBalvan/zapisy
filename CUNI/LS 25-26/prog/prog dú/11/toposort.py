#!/usr/bin/python3

class Graph():
    def __init__(self, edge_list):
        self.E = set(edge_list)
        self.V = range(self._n_vertices())

    def _n_vertices(self):
        max = 0
        for edge in self.E:
            a, b = edge
            if a > max: max = a
            if b > max: max = b
        return max+1

    def sources(self):
        not_sources = set()
        for e in self.E:
            source, target = e
            not_sources.add(target)
        return set(self.V) - not_sources

    def without_vertex(self, v):
        new_graph = Graph({ e for e in self.E if e[0] != v and e[1] != v })
        new_graph.V = set(self.V) - {v}
        return new_graph

    def topological_sortings(self):
        if len(self.V) == 0:         # no vertices
            yield []
            return

        # otherwise there might be some source vertices
        for source in self.sources():
            g = self.without_vertex(source)
            for ts in g.topological_sortings():
                yield [source] + ts
        return

    def number_of_topological_sortings(graph):
        if len(graph.V) == 0: return 1

        return sum([ graph.without_vertex(source).number_of_topological_sortings()
                     for source in graph.sources() ])


G4 = Graph({(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 5), (3, 6), (4, 6), (5, 6)})
for ts in G4.topological_sortings():
    for cislo in ts:
        print(cislo, end=", ")
    print()
print("Count", G4.number_of_topological_sortings())
