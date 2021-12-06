class Solution:
    def generate(self, numRows):
        triangle = [[1]]
        for i in range(1, numRows):
            layer = [1]
            for j in range(len(triangle[i - 1]) - 1):
                layer.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
            layer.append(1)
            triangle.append(layer)
        return triangle
    
s = Solution()
print(s.generate(4))