class Solution:
    def rotate(self, nums, k):
        i = 0
        moving = nums[i]
        cnt = 0
        front = 0
        while cnt < len(nums):
            i = (i + k) % len(nums)
            nums[i], moving = moving, nums[i]
            cnt += 1
            if i == front:
                front += 1
                i = front
                moving = nums[i]
            print(nums)

            

s = Solution()
s.rotate([-1,-100,3,99], 2)