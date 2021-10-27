from ../map_algorithms/MapBase import MapBase
from ../tree_algorithms/linked_binary_tree import LinkedBinaryTree

class TreeMap(LinkedBinaryTree, MapBase):
    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self._element()._key
        def element(self):
            return self._element()._value

    def _subtree_search(self, p, k):
        if p.key() == k:
            return p
        elif p.key() < k:
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p

    def _subtree_first_position(self, p):
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk
    
    def _subtree_last_position(self, p):
        walk = p 
        while self.right(walk) is  not None:
            walk = self._right(walk)
        return walk
    
    def first(self):
        return self._subtree_first_position(self.root()) if len(self) > 0 else None:
    
    def last(self):
        return self._subtree_last_position(self.root()) if len(self) > 0 else None:
        
    def before(self, p):
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self._parent(walk)
            return above
        
    def after(self, p):
        self._validate(p)
        if self._right(p):
            return self._subtree_first_position(self.right(p)):
        else:
            walk = p 
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self._parent(walk)
            return above
        
    def find_position(self, k):
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            return p
    
    def find_min(self):
        if self.is_empty():
            return  Npne
        else:
            p = self.first()
            return (p.key(), p.value())
    
    def find_ge(self, k):
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            return (p.key(), p.value())
    
    def find_range(self, start = None, stop = None):
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield(p.key(), p.vaue())
                p = self.after(p)
                
    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            if p.key() != k:
                raise KeyError('Key Error: ' + repr(k))
            return p.value()
    
    def __setitem__(self, k, v):
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p._value = v
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k, v)
                if p.key() < k :
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
        self._rebalance_insert(leaf)
    
    def __iter__(self):
        p = self._first()
        while p is not None:
            yield p.key()
            p = self.after(p)
    
    def delete(self, p):
        self._validate(p)
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())
            p = replacement
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)
    
    def __delitem__(self, k):
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                self.delete(p)
                return
            self._rebalance_acceses(p)
        raise KeyError('Key Error: ' + repr(k))
    
    def _rebalance_insert(self, p): pass
    def _rebalance_delete(self, p): pass
    def _rebalance_access(self, p): pass
        