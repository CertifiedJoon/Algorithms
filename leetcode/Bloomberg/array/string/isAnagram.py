class Solution:
    def isAnagram(self, s, t):
        letters = [0] * 26
        if len(s) != len(t):
            return False
        for x, y in zip(s, t):
            letters[ord(x) - ord('a')] += 1
            letters[ord(y) - ord('a')] -= 1
        for count in letters:
            if count != 0:
                return False
        return True

s = Solution()
print(s.isAnagram("anagram", "gramana"))