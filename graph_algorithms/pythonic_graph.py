class Graph:
    class Vertex:
        __slots__ = '_element'
        def __init__(self, e):
            self._element = e
        
        def element(self):
            return self._element
        
        def __hash__(self):
            return hash(id(self))
        
    class Edge:
        __slots__ = '_origin', '_destination', '_element'
        def __init__(self, o, d, e):
            self._origin = o
            self._destination = d
            self._element = e
        
        def element(self):
            return self._element
    
        def opposite(self, v):
            return self._destination if v is self._origin else self._origin
        
        def __hash__(self):
            return hash((self._origin, self._destination))
        
        def end_points(self):
            return (self._origin, self._destination)
        
    def __init__(self, directed = False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing
        
    def is_directed(self):
        return self._incoming is not self._outgoing
    
    def vertex_count(self):
        return len(self._outgoing)
    
    def vertices(self):
        for vertex in self._outgoing.keys():
            yield vertex
            
    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2
    
    def edges(self):
        for secondary_map in self._outgoing.values():
            for edge in secondary_map.values():
                yield edge
                
    def get_edge(self, v, u):
        return self._outgoing[v].get(u)
    
    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    
    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
    
    def insert_vertex(self, e):
        v = self.Vertex(e)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v
    
    def insert_edge(self, v, u, e):
        edge = self.Edge(v, u, e)
        self._outgoing[v][u] = edge
        self._incoming[u][v] = edge
        
    def remove_edge(self, edge):
        u, v = edge.end_points()
        del self._outgoing[u][v]
        del self._incoming[v][u]
        
    def transposed(self):
        import copy
        tp = copy.deepcopy(self)
        for edge in self.edges():
            u, v = edge.end_points()
            tp.insert_edge(u, v, edge.element())
            tp.remove_edge(edge)
        return tp


def topological_sort(g):
    incount = {}
    topo = []
    ready = []
    for v in g.vertices():
        incount[v] = g.degree(v, False)
        if incount[v] == 0:
            ready.append(v)
    while ready:
        u = ready.pop()
        topo.append(u)
        for edge in g.incident_edges(u):
            v = edge.opposite(u)
            incount[v] -= 1
            if incount[v] == 0:
                ready.append(v)
    return topo

def fill_order(g, u, stack, visited):
    visited.add(u)
    for edge in g.incident_edges(u):
        v = edge.opposite(u)
        if v not in visited:
            fill_order(g, v, stack, visited)
    stack.append(u)
    
def transposed(g): 
    """Need a clever way of transposing"""
    tp = Graph(True)
    for edge in g.edges():
        u, v  = edge.end_points()
        
        origin = tp.insert_vertex(u.element())
        dest = tp.insert_vertex(v.element())
        tp.insert_edge(dest, origin, edge.element())
    return tp

def dfs(g, u, order, visited):
    order.append(u)
    visited.add(u)
    for edge in g.incident_edges(u):
        v = edge.opposite(u)
        if v not in visited:
            dfs(g, v, order, visited)

def kosaraju(g, u):
    stack = []
    scc = []
    visited = set()
    fill_order(g, u, stack, set())
    tp = g.transposed()
    while stack:
        connected = []
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            dfs(tp, u, connected, set())
            scc.append(connected)
    return scc
                

if __name__ == "__main__":
    g = Graph(True)
    v1 = g.insert_vertex(1)
    v2 = g.insert_vertex(2)
    v3 = g.insert_vertex(3)
    v4 = g.insert_vertex(4)
    v5 = g.insert_vertex(5)
    v6 = g.insert_vertex(6)
    
    g.insert_edge(v1, v2, 1)
    g.insert_edge(v2, v3, 1)
    g.insert_edge(v3, v1, 1)
    g.insert_edge(v2, v4, 1)
    g.insert_edge(v4, v5, 1)
    g.insert_edge(v5, v6, 1)
    g.insert_edge(v6, v4, 1)
    
    # print([v.element() for v in topological_sort(g)])
    print(kosaraju(g, v1))