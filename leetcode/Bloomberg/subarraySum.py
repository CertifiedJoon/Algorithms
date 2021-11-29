class Solution:
    def subarraySum(self, nums, k):
        ans = 0
        sums = {}
        
        running = 0
        running_sums = [0] * len(nums)
        for i in range(len(nums)):
            running += nums[i]
            running_sums[i] = running
        
        for i in range(len(nums)):
            running += nums[i]