class Solution:
    def compress(self, chars):
        write_at = 0
        count = 0
        for i, char in enumerate(chars):
            if (i != 0 and chars[i - 1] != chars[i]):
                chars[write_at] = chars[i - 1]
                write_at += 1
                if count > 1:
                    print(count)
                    for digit in str(count):
                        chars[write_at] = digit
                        write_at += 1
                count = 0
            elif i != 0:
                count += 1
            if i == len(chars) - 1:
                
        for _ in range(write_at, len(chars)):
            chars.pop()
        return write_at
    
s = Solution()
strs = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(s.compress(strs), strs)