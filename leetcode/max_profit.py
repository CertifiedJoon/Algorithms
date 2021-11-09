import time
import unittest
from collections import defaultdict

def max_profit(nums):
    if not nums:
        raise ValueError("empty list has been passed")
    profit = 0
    bought = nums[0]
    for price in nums:
        if bought > price:
            profit = 0
            bought = price
        else:
            if profit < price - bought:
                profit = price - bought
    return profit



class Test(unittest.TestCase):
    test_cases = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0), 
        ([7,1,5,3,6,4,0], 0),
        ([7,1,5,3,6,4,0,6], 6),
        ([0], 0)
    ]
    test_functions = [
        max_profit
    ]
    
    def test_two_sums(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for given, expected in self.test_cases:
                for solve in self.test_functions:
                    start = time.process_time()
                    assert(
                        solve(given) == expected
                    ),f"{solve.__name__} failed at {given[0], given[1]}"
                    function_runtimes[solve.__name__] += (
                        time.process_time() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()