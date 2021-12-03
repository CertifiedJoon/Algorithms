class Solution:
    def twoSum(self, nums, target):
        """ nums is sorted """
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                return [i,j]
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        raise runtimeError("Not found")