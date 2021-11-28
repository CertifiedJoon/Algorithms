import time
import unittest
from collections import defaultdict, Counter

class Solution:
    def group_anagrams(self, strs):
        anagrams = defaultdict(list)
        for s in strs:
            mapped = [0] * 26
            for c in s:
                mapped[ord(c) - ord('a')] += 1
            anagrams[tuple(mapped)].append(s)
        print(list(anagrams.values()))
        return list(anagrams.values())

class Test(unittest.TestCase):
    test_cases = [
        [["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]]
    ]
    test_functions = [
        Solution.group_anagrams
    ]
    
    def test_group_anagrams(self):
        num_runs = 1
        function_runtimes = defaultdict(float)
        solution = Solution()
        for _ in range(num_runs):
            for given, expected in self.test_cases:
                for solve in self.test_functions:
                    start = time.process_time()
                    assert(
                        solve(solution, given) == expected
                    ),f"{solve.__name__} failed at {given}"
                    function_runtime() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()