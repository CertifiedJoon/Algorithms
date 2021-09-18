import queue
import time
from collections import defaultdict
import random
import unittest

class DirectedGraph:
    def __init__(self, adj = None):
        self._adjacency_list = adj
    
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
        return level, parents


    def dfs(self):
        parents = {}
        initial = set()
        to_visit_stack = []
        
        for vertex in self:
            if vertex not in parents:
                initial.add(vertex)
            else:
                continue
                
            to_visit_stack.append(vertex)
            
            while to_visit_stack:
                v = to_visit_stack.pop()
                
                for neighbor in self._adjacency_list[v]:
                    if neighbor not in parents:
                        parents[neighbor] = v
                        to_visit_stack.append(neighbor)
        
        return initial, parents
        
    
    def rec_dfs(self):
        parents = {}
        for s in self._adjacency_list:
            if s not in parents:
                parents[s] = None
                self.dfs_visit(s, parents)
        
    def dfs_visit(self, s, parents):
        for vertex in self._adjacency_list[s]:
            if vertex not in parents:
                parents[vertex] = s 
                self.dfs_visit(vertex, parents)
                
    def contains_cycle(self, 1):
        to_visit = []
        visited = set()
        popped = set()
        for s in self:
            to_visit.append(s)
            while to_visit:
                anc = to_visit.pop()
                popped.append(anc)
                for chd in self._adjacency_list[anc]:
                    if chd in popped:
                        return True
                    if chd not in visited:
                        to_visit.append(chd)
        return False
    
    def topological_sort(self):
        order = []
        visited = set()
        for s in self:
            to_visit.append(s)
            while to_visit:
                anc = to_visit.pop()
                order.append(anc)
                for chd in self._adjacency_list[anc]:
                    if chd not in visited:
                        to_visit.append(chd)
        return order

if __name__ == "__main__":
    dg = DirectedGraph({1: {2,3}, 2: {4, 5}, 3: {6}, 4: {7}, 5: {7}, 6: {5, 7}, 7:{2}})
    print(dg.bfs())
    print(dg.dfs())
    print(dg.rec_dfs())
    print(dg.contains_cycle())
    print(dg.topological_sort())