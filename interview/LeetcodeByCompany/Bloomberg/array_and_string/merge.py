class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = len(nums1) - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:   
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        if j >= 0:
            nums1[:j + 1] = nums2[:j + 1]

s = Solution()
nums = [0]
s.merge(nums, 0, [1], 1)
print(nums)