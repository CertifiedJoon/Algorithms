class Solution:
    def decodeString(self, s):
        if not s:
            return ""
        print(s)
        i = 0
        ret = ""
        while i < len(s):
            digit_start = i 
            while s[i].isdigit():
                i += 1
            k = int(s[digit_start: i])
            bracket_count = 1
            i += 1
            to_decode = []
            decoded_part = []
            while True:
                if s[i] == '[':
                    bracket_count += 1
                elif s[i] == ']':
                    bracket_count -= 1
                if not bracket_count: 
                    i += 1
                    break 
                to_decode.append(s[i])
                i += 1
            if not to_decode:
                ret +=  ("".join(decoded_part) * k)
            else:
                ret += (("".join(decoded_part) + self.decodeString("".join(to_decode))) * k)
        return ret

s = Solution()
print (s.decodeString("10[aabb2[c]aabb2[d]]2[c]"))