import collections
class Solution:
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        max_freq = max(count.values())
        bucket = [[] for _ in range(max_freq + 1)]
        for word, cnt in count.items():
            bucket[cnt].append(word)
        ret = []
        for i in range(len(bucket) - 1, -1, -1):
            bucket[i].sort()
            for word in bucket[i]:
                ret.append(word)
                k -= 1
                if not k:
                    break
            if not k:
                break
        return ret
