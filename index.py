nums1 = [1,2,3,4,5,6,7,8]
nums2 = [1,2,3,4,5,6,7,8]

def isSame(nums1, nums2):
    while True:
        n1 = iterate(nums1)
        n2 = iterate(nums2)
        print(n1, n2)
        if n1 != n2:
            return False
    return True

def iterate(nums):
    for n in nums:
        yield n

print(isSame(nums1, nums2))