class Solution:
    def alienOrder(self, words):
        outgoing, incoming = {}, {}
        for c in "".join(words):
            if c not in incoming:
                incoming[c] = set()
            if c not in outgoing:
                outgoing[c] = set()
        
        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    outgoing[words[i][j]].add(words[i + 1][j])
                    incoming[words[i + 1][j]].add(words[i][j])
                    break
                if j + 1 == len(words[i + 1]) and len(words[i]) > j + 1:
                    return ""
        
        return "" if self.contains_cycle() else self.top_sort(incoming, outgoing)
    
    def top_sort(self, incoming, outgoing):
        degree = {}
        to_visit = []
        for c, inc in incoming.items():
            degree[c] = len(inc)
            if degree[c] == 0:
                to_visit.append(c)
        topo = []
        while to_visit:
            c = to_visit.pop()
            topo.append(c)
            for d in outgoing[c]:
                degree[d] -= 1
                if degree[d] == 0:
                    to_visit.append(d)
        
        return "".join(topo)

    def contains_cycle(self, outgoing):   
        STATUS_STARTED = 1
        STATUS_FINISHED = 2
        for vertex in outgoing:
            statuses = {}
            to_visit = [vertex]
            while to_visit:
                u = to_visit.pop()
                if u in statuses:
                    if statuses[u] == STATUS_STARTED:
                        statuses[u] = STATUS_FINISHED
                else:
                    statuses[u] = STATUS_STARTED
                    to_visit.append(u)
                for v in outgoing[u]:
                    if v in statuses:
                        if statuses[v] == STATUS_STARTED:
                            return True
                    else:
                        to_visit.append(v)
        return False

s = Solution()
print(s.alienOrder(["z","x","a","zb","zx"]))