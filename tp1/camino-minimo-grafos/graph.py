# -*- coding: utf-8 -*-


class Graph(object):
    """Grafo no dirigido con un número fijo de vértices.

    Los vértices son siempre números enteros no negativos. El primer vértice
    es 0.

    El grafo se crea vacío, se añaden las aristas con add_edge(). Una vez
    creadas, las aristas no se pueden eliminar, pero siempre se puede añadir
    nuevas aristas.
    """

    def __init__(g, V):
        """ Construye un grafo sin aristas de V vértices. """
        g._a = [[] for _ in range(V)]  # _a es la matriz de adyacencias
        g._i = [[] for _ in range(V)]  # _i es la matriz de incidencias

    def V(g):
        """ Número de vértices en el grafo. """
        return len(g._a)

    def E(g):
        """ Número de aristas en el grafo. """
        return sum(len(x) for x in g._i)

    def adj_e(g, v):
        """ Itera sobre los aristas incidentes desde v. """
        return iter(g._i[v])

    def adj(g, v):
        """ Itera sobre los vértices adyacentes a v. """
        return iter(g._a[v])

    def add_edge(g, u, v, weight=0):
        """ Añade una arista al grafo. Devuelve la arista agregada """
        a = Edge(u, v, weight)
        g._i[u].append(a)
        g._a[u].append(v)
        return a

    def __iter__(g):
        """Itera de 0 a V."""
        return iter(range(g.V()))

    def iter_edges(g):
        """Itera sobre todas las aristas del grafo.

        Las aristas devueltas tienen los siguientes atributos de solo lectura:
            - e.src
            - e.dst
            - e.weight
        """
        return iter(edge for edges in g._a for edge in edges)

    def has_node(g, v):
        return v < len(g._a)

    @classmethod
    def from_dict(cls, d):
        """ Toma un diccionario, compuesto de la siguiente manera:
            {
                nodo: [nodo_adjacente, nodo_adjacente2],
                nodo2: [...]
            }
            Por ejemplo:
            {
                1: [2, 3, 4, 5]
                2: [3],
                4: [5]
            }
        """
        max_node = max(max(d.keys()), max(v for values in d.values() for v in values))
        g = cls(max_node + 1)
        for src, v in d.items():
            for dst in v:
                if g.has_node(dst):
                    g.add_edge(src, dst)
        return g


class Edge(object):
    """ Arista de un grafo. """

    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight
