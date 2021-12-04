class Solution:
    def alienOrder(self, words):
        outgoing, incoming = defaultdict(set()), defaultdict(set())
        for word in words:
            for i, c in enumerate(word):
                outgoing[c].add([d for d in word[i:] if d != c])
                incoming[c].add([d for d in word[:i] if d != c])
        degree = {}
        for c, smaller in incoming.items():
            degree[c] = len(smaller)
        
        to_visit = [c for c in incoming if incoming[c] == 0]
        topo = []

        while to_visit:
            c = to_visit.pop()
            topo.append(c)
            for d in outgoing[c]:
                degree[d] -= 1
                if not degree[d]:
                    to_visit.append(d)
        
        return topo