import time
import unittest
from collections import defaultdict
import random
from operator import itemgetter

class Solution:
    def merge_intervals(self, intervals):
        intervals.sort(key=itemgetter(0))
        start, end = intervals[0]
        merged = []
        for interval in intervals:
            if end >= interval[0]:
                start = min(interval[0], start)
                end = max(interval[1], end)
            else:
                merged.append([start, end])
                start = interval[0]
                end = interval[1]
        merged.append([start, end])
        return merged
    
    def fromleetcode(self, intervals):
        intervals.sort(key =lambda x: x[0])
        merged =[]
        for i in intervals:
			# if the list of merged intervals is empty 
			# or if the current interval does not overlap with the previous,
			# simply append it.
            if not merged or merged[-1][-1] < i[0]:
                merged.append(i)
			# otherwise, there is overlap,
			#so we merge the current and previous intervals.
            else:
                merged[-1][-1] = max(merged[-1][-1], i[-1])
        return merged

class Test(unittest.TestCase):
    test_cases = [
    ]
    test_functions = [
        Solution.merge_intervals
    ]

    def test(self):
        num_runs = 100
        num_cases = 1000
        function_runtimes = defaultdict(float)
        solution = Solution()
        for _ in range(num_cases):
            n = random.randrange(1,10)
            given = []
            for _ in range(n):
                mid = random.randrange(1,100)
                start = mid - random.randrange(0, mid)
                end = mid + random.randrange(mid, 100)
                given.append([start, end])
            self.test_cases.append((given, solution.fromleetcode(given)))
        for _ in range(num_runs):
            for given, expected in self.test_cases:
                for solve in self.test_functions:
                    start = time.process_time()
                    assert(
                        solve(solution, given) == expected
                    ),f"{solve.__name__} failed at {given}"
                    function_runtimes[solve.__name__] += (
                        time.process_time() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()