import queue
from collections import defaultdict

class DirectedGraph:
    def __init__(self):
        self._adjacency_list = {}
    
    def add_node(self, src, des):
        if src not in self._adjacency_list:
            self._adjacency_list[src] = set()
        self._adjacency_list[src].add(des)
    
    def __iter__(self):
        for s in self._adjacency_list:
            yield s   
    
    def bfs(self, src):
        parents = {src: None}
        frontier = [src]
        i = 1
        level = {s : 0}
        
        while frontier: 
            next_step = []
            for u in frontier:
                for v in self._adjacency_list[u]:
                    if v not in level:
                        level[v] = i
                        parents[v] = u
                        next_step.append(v)
            frontier = next_step
            i +=1 
        