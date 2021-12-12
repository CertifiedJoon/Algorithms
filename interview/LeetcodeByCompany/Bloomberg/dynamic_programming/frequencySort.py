import collections

class Solution:
    def frequencySortSpeed(self, s: str) -> str:
        count = collections.Counter(s)
        max_freq = max(count.values())
        bucket = [[] for _ in range(max_freq + 1)]
        string_builder = []
        for c, i in count.items():
            bucket[i].append(c)
            
        for i in range(len(bucket) - 1, 0, -1):
            for c in bucket[i]:
                string_builder.append(c * i)
        
        return "".join(string_builder)

    def frequencySortMemory(self, s):
        count = collections.Counter(s)
        string_builder = []
        for c, i in count.most_common():
            string_builder.append(c * i)
        return "".join(string_builder)