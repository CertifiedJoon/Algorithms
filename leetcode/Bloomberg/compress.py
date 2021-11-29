import time
import unittest
from collections import defaultdict
import random 
import copy

class Solution:
    def compress(self, chars):
        write_at = 0
        count = 0
        curr = chars[0]
        for i in range(len(chars)):
            if chars[i] == curr:
                count += 1
            else:
                write_at = self.write(self, chars, curr, count, write_at)
                count = 1
                curr = chars[i]
        write_at = self.write(self, chars, curr, count, write_at)
        del chars[write_at:]
        return write_at
    
    def write(self, chars, letter, count, i):
        chars[i] = letter
        i += 1
        if count > 1:
            for c in str(count):
                chars[i] = c
                i += 1
        return i

class Test(unittest.TestCase):
    test_cases = [

    ]
    test_functions = [
        Solution.compress
    ]
    
    def test(self):
        num_runs = 1
        num_cases = 10000
        function_runtimes = defaultdict(float)

        for _ in range(num_cases):
            arr = []
            expected = []
            for char in ['a', 'b', 'c', 'd', 'e']:
                rep = random.randrange(23)
                arr.extend([char] * rep)
                if rep > 0:
                    expected.append(char)
                if rep > 1:
                    for c in str(rep):
                        expected.append(c)
            self.test_cases.append([arr, expected])

        s = Solution
        for _ in range(num_runs):
            for given, expected in self.test_cases:
                for solve in self.test_functions:
                    copied = copy.deepcopy(given)
                    start = time.process_time()
                    assert(
                        solve(s, copied) == len(expected) and copied == expected
                    ),f"{solve.__name__} failed at {given}, \n got {copied} vs {expected}"
                    function_runtimes[solve.__name__] += (
                        time.process_time() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()

