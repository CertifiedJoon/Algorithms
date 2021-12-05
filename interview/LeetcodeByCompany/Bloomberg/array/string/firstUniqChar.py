class Solution:
    def firstUniqChar(self, s):
        seen = [len(s)] * 26
        for i, c in enumerate(s):
            if seen[ord(c) - ord('a')] == len(s):
                seen[ord(c) - ord('a')] = i
            else:
                seen[ord(c) - ord('a')] = len(s) + 1
        first = len(s)
        for i in range(len(seen)):
            if seen[i] < len(s):
                first = min(first, seen[i])
        return first if first != len(s) else -1

        
s = Solution()
print(s.firstUniqChar("aabb"))