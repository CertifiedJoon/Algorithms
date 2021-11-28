class Solution:
    def spiralOrder(self, m):
        i_start, i_end = 0, len(m[0]) - 1
        j_start, j_end = 0, len(m) - 1
        ret = []
        while i_start <= i_end and j_start <= j_end:
            for i in range(i_start, i_end + 1):
                ret.append(m[j_start][i])
            for j in range(j_start + 1, j_end + 1):
                ret.append(m[j][i_end])
            if j_start != j_end:
                for i in range(i_end - 1, i_start - 1, -1):
                    ret.append(m[j_end][i])
            if i_start != i_end:
                for j in range(j_end - 1, j_start, -1):
                    ret.append(m[j][i_start])
            i_start, j_start = i_start + 1, j_start + 1
            i_end, j_end = i_end - 1, j_end - 1
        return ret

s = Solution()
print(s.spiralOrder([[6,9,7]]))