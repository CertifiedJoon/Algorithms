class Solution:
    def twoSum(self, nums, target):
        """dicionary mapping of nums[i] : i, search for target-nums[i] in dictionary.keys(). O(n)"""
        mapped = {}
        for i in range(len(nums)):
            if target - nums[i] in mapped and i != mapped[target - nums[i]]:
                return [i, mapped[target - nums[i]]]
            mapped[nums[i]] = i
            
s = Solution()
print(s.twoSum([3,2,4], 6))