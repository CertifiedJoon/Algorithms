import queue
import time
from collections import defaultdict
import random
import unittest

class DirectedGraph:
    def __init__(self, adj=None):
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
                
    def contains_cycle(self):
        to_visit_stack = []
        
        for vertex in self:
            visited = set()
            to_visit_stack.append(vertex)
            while to_visit_stack:
                v = to_visit_stack.pop()

                for neighbor in self._adjacency_list[v]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        to_visit_stack.append(neighbor)
                    else:
                        return False
        return True
    
    def topological_sort(self):
        STATUS_STARTED = 1
        STATUS_FINISHED = 0
        statuses = {}
        order = []
        
        for vertex in self:
            to_visit = [vertex]
            if vertex in statuses:
                if statuses[vertex] = STATUS_STARTED:
                    statuses[vertex] = STATUS_FINISHED
                    order.append(vertex)
            else:
                statuses[vertex] = STATUS_STARTED
                to_visit.append(vertex)
            
            to_visit.extend([neighbor for neighbor in self._adjacency_list[vertex] if neighbor not in statuses])
        
        order.reverse()
        
        return order
    
        