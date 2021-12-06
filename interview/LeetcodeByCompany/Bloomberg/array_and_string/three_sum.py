import time
import unittest
from collections import defaultdict
import random 

class Solution:
    def threeSumNoSort(self, nums):
        res, dups = set(), set()
        seen = {}
        for i, vali in enumerate(nums):
            if vali not in dups:
                dups.add(vali)
                for j, valj in enumerate(nums[i + 1:]):
                    complement = -vali - valj
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted([vali, valj, complement])))
                    seen[valj] = i
        return res


    def threeSumExtended(self, nums): 
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res
    
    def twoSumII(self, nums, first, res):
        lo = first + 1
        hi = len(nums) - 1
        while lo < hi:
            summed = nums[first] + nums[lo] + nums[hi]
            if summed < 0:
                lo += 1
            elif summed > 0:
                hi -= 1
            else:
                res.append([nums[first], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1

class Test(unittest.TestCase):
    test_cases = [
        [[-1,0,1,1,1,1,1,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]],
        [[-1,0,1,1,1,1,1,1,2,2,-1,-4], [[-1,-1,2],[-1,0,1],[-4,2,2]]],
        [[-4,-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1],[-4,0,4]]],
        [[],[]],
        [[0],[]]
    ]
    test_functions = [
        Solution.threeSumNoSort,
        Solution.threeSumExtended
    ]
    
    def test(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for given, expected in self.test_cases:
                for solve in self.test_functions:
                    s= Solution()
                    start = time.process_time()
                    ans = solve(s, given)
                    function_runtimes[solve.__name__] += (
                        time.process_time() - start
                    ) * 1000
                    solved = True
                    for s in ans:
                        if s not in expected:
                            solved = False
                    assert(
                        solved
                    ),f"{solve.__name__} failed at {given}"
                    

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()