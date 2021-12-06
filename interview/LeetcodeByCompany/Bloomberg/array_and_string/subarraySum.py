import time
import unittest
from collections import defaultdict
import random 

def subarraySum(nums, k):
    running_sums = defaultdict(int)
    runner = 0
    cnt = 0
    running_sums[0] = 1
    for i in range(1, len(nums) + 1):
        runner += nums[i - 1]
        cnt += running_sums[runner - k]
        running_sums[runner] += 1  
    return cnt



class Test(unittest.TestCase):
    test_cases = [
    ]
    test_functions = [
        subarraySum
    ]
    
    def test(self):
        num_runs = 1
        num_cases = 10000
        function_runtimes = defaultdict(float)
        
        for _ in range(num_cases):
            nums = random.choices(range(-9, 10), k=5)
            k = random.randrange(-9,10)
            cnt = 0
            for i in range(1, len(nums) + 1):
                for j in range(i):
                    if sum(nums[j:i]) == k:
                        cnt += 1
            self.test_cases.append(((nums, k), cnt))

        for _ in range(num_runs):
            for given, expected in self.test_cases:
                for solve in self.test_functions:
                    start = time.process_time()
                    assert(
                        solve(given[0], given[1]) == expected
                    ),f"{solve.__name__} failed at {given, expected}"
                    function_runtimes[solve.__name__] += (
                        time.process_time() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()