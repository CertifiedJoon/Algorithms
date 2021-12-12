class Solution:
    def trap(self, height):
        """
        DP solution
        """
        leftmax = rightmax = 0
        left, right = 0, len(height) - 1
        total = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftmax:
                    leftmax = height[left]
                else:
                    total += leftmax - height[left]
            else:
                if height[right] >= rightmax:
                    rightmax = height[right]
                else:
                    total += rightmax - height[right]
        return total
    
    def trap2(self, height):
        """
        global maximum two pass
        """