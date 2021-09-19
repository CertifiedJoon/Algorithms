from collections import namedtuple
import queue
import pysnooper

Edge = namedtuple('Edge', ['vertex', 'weight'])
class DirectedWeightedGraph:
    def __init__(self, v_cnt, adj_list):
        self._v_cnt = v_cnt
        self._adj_list = [[] for _ in range(v_cnt)]
        for i in range(v_cnt):
            for edge in adj_list[i]:
                self._adj_list[i].append(Edge(edge[0], edge[1]))
        
    def iter_neighbors(self, vi):
        """
        variable 
            vi = vertex at index i 
        function
            iterates through neighbor of the vertex at given index vi
        """
        for nb in self._adj_list[vi]:
            yield nb
        
    def iter_vertices(self):
        """
        function
            iterates through all the vertices by Index
        """
        for vi in range(self._v_cnt):
            yield vi
            
    @pysnooper.snoop()
    def dijkstra_min_heap(self, s, e):
        """
        variable
            s : starting vertex
            e : destination vertex
        function
            calculate dijkstra shortest path for each vertex starting from s
            return tuple(shortest path from s to e including s and e, shortest path length)
        """
        
        NO_PRED = -1
        NO_PATH = float('inf')
        
        best_pred = [NO_PRED for _ in range(self._v_cnt)]
        sp_len = [NO_PATH for _ in range(self._v_cnt)]
        pq = queue.PriorityQueue()
        pq.put([0, s])
        sp_len[0] = 0
        unfinished_vertex = set([i for i in range(self._v_cnt)])
        
        while unfinished_vertex:
            v = pq.get()
            while v[1] not in unfinished_vertex:
                v = pq.get()
            unfinished_vertex.remove(v[1])
            for edge in self.iter_neighbors(v[1]):
                if sp_len[edge.vertex] > sp_len[v[1]] + edge.weight:
                    best_pred[edge.vertex] = v[1]
                    sp_len[edge.vertex] = sp_len[v[1]] + edge.weight
                pq.put([sp_len[edge.vertex], edge.vertex])
        
        shortest_path = []
        curr = e
        
        while curr != s:
            shortest_path.append(curr)
            curr = best_pred[curr]
            
        shortest_path.append(s)
        shortest_path.reverse()
        
        return(shortest_path, sp_len[e])
    
    def dijkstra_fib_heap(self, s, e):
        
    
if __name__ == "__main__":
    test_case = [
        [(1, 10), (2, 3)],
        [(3, 2) , (2, 1)],
        [(1, 4) , (3, 8), (4, 2)],
        [(4, 7)],
        [(3, 9)]
    ]
    
    dwg = DirectedWeightedGraph(5, test_case)
    print(dwg.dijkstra_min_heap(0, 3))