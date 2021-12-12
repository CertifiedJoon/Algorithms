class Solution:
    def rotate(self, nums, k):
        temp = nums[0]
        i = 0
        while True:
            swapi = (i + k) % len(nums)
            print(nums[swapi], temp)
            nums[swapi], temp = temp, nums[swapi]
            i = swapi
            if i == 0:
                if len(nums) % k == 0:
                    i += 1
                    temp = nums[i + 1]
                else: 
                    break

s = Solution()
print(s.rotate([-1,-100,3,99],))
