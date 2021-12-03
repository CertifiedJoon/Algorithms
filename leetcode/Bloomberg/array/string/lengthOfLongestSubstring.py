class Solution:
    def lengthOfLongestSubstring(self, s):
        """ sliding window """
        ans = i = 0
        m = {}
        for j in range(len(s)):
            if s[j] in m:
                i = max(m[s[j]] + 1, i)
            ans = max(ans, j - i + 1)
            m[s[j]] = j
            print(ans, m)
        return ans
            

s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))