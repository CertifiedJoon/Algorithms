class Solution:
    def removeDuplicates(self, nums):
        write_at = 0
        duplicated_character = ""
        for i in range(len(nums)):
            if nums[i] != duplicated_character:
                nums[write_at] = nums[i]
                duplicated_character = nums[i]
                write_at += 1
            else:
                nums[i] = "_"
        nums = nums[:write_at]