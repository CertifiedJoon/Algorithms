from collections import namedtuple
import queue

class DirectedWeightedGraph:
    def __init__(self, v_cnt, adj_list):
        self._v_cnt = v_cnt 
        self._adj_list = adj_list
        
    def iter_neighbors(self, vi):
        """
        variable 
            vi = vertex at index i 
        function
            iterates through neighbor of the vertex at given index vi
        """
        for nb in self._adj_list(vi):
            yield nb
        
    def iter_vertices(self):
        """
        function
            iterates through all the vertices by Index
        """
        for vi in range(self._v_cnt):
            yield vi
             
    def dijkstra(self, s, e):
        """
        gotta add function prose and add Edge namedtuple
        """
        NO_PRED = -1
        NO_PATH = float('inf')
        
        best_pred = [NO_PRED for _ in range(self._v_cnt)]
        sp_len = [NO_PATH for _ in range(self._v_cnt)]
        pq = queue.PriorityQueue()
        pq.put([0, s])
        sp_len[0] = 0
        
        while pq:
            v = pq.get()
            for edge in self.iter_neighbors(v[1]):
                if sp_len[edge.vertex] < sp_len[v[1]] + edge.weight:
                    best_pred[edge.vertex] = v[1]
                    sp_len[edge.vertex] = sp_len[v[1]] + edge.weight
                pq.put([sp_len[edge.vertex], edge.vertex])
        
        shortest_path = []
        curr = e
        
        while curr != s:
            shortest_path.append([best_pred[curr]])
            curr = best_pred[curr]
            
        shortest_path.append(s)
        shortest_path.reverse()
        
        return(shortest_path, sp_len[e])