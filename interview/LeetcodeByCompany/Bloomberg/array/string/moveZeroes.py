class Solution:
    def moveZeroes(self, nums):
        zeroLastFoundAt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zeroLastFoundAt] = nums[zeroLastFoundAt], nums[i]
                zeroLastFoundAt += 1

s = Solution()
nums = [1,2,0,3,0,4,5]
s.moveZeroes(nums)
print(nums)
