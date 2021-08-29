import time
import unittest
from collections import defaultdict
import random

# RK_Search
def rabin_karp_search(haystack, needle):
    d = len(set(c for c in haystack))
    m = len(haystack)
    n = len(needle)
    
    hash_needle = rk_hash(needle,d)
    hash_haystack = rk_hash(haystack[0:n],d)
    
    for i in range(m - n + 1):
        if hash_needle == hash_haystack and needle == haystack[i:i+n]:
            return i
        
        if i + n < m:
            hash_haystack = d * (hash_haystack - pow(d, n-1) * ord(haystack[i])
            ) + (ord(haystack[i + n]))
        
    return -1

def rk_hash(s, n_chr_set):
    ret_hash = 0
    for c in s:
        ret_hash = ret_hash * n_chr_set + ord(c)
    return ret_hash

# KMP Search
def knuth_morris_pratt_search(haystack, needle):
    m = len(haystack)
    n = len(needle)
    lps = calc_lps(needle)
    i = j = 0
    
    while (i < m and j < n):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        if j == n:
            return i - n
        
        if i < m and haystack[i] != needle[j]:
            if j:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1
                
def calc_lps(needle):
    n = len(needle)
    ret = [0 for _ in range(n)]
    common_length = 0
    i = 1
    
    while (i < n):
        if needle[i] == needle[common_length]:
            common_length += 1
            ret[i] = common_length
            i += 1
        elif (common_length):
            common_length = ret[common_length - 1]
        else:
            i += 1
    
    return ret
    
# BM Search
def boyer_moore_search_bad_char(haystack, needle):
    bad_char = bad_char_heurestics(needle)
    m = len(haystack)
    n = len(needle)
    s = 0
    while (s <= m - n):
        j = n - 1
        while j >= 0 and haystack[s + j] == needle[j]:
            j -= 1
        if j == -1:
            return s
        else:
            if bad_char[ord(haystack[s + j])] == -1:
                s += n
            else:
                s += max(1, j - bad_char[ord(haystack[s + j])])
    return -1

def bad_char_heurestics(needle):
    NO_OF_CHAR = 128
    bad_char = [-1] * NO_OF_CHAR
    for i in range(len(needle)):
        bad_char[ord(needle[i])] = i
    return bad_char
    
    
    
    
    
class Test(unittest.TestCase):
    test_cases_real_life = [
        ("For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.", "For sequences", 55),
        ("algorithm demonstration. This is the primary type of problem and solution that the text is concerned with. As such, solutions should not use standard library functions in cases that would make it unnecessary to implement the algorithm. The goal of these solutions should be to have an easy to understand solution that demonstrates understanding of the algori",
        "library functions in cases that would make it unnecessary to implement the algorithm", 150),
        ("If neither weights nor cum_weights are specified, selections are made with equal probability. If a weights sequence is supplied, it must be the same length as the population sequence. It is a TypeError to specify both weights and cum_weights.", "cum_weights.", 230),
        ("On the real line, there are functions to compute uniform, normal (Gaussian), lognormal, negative exponential, gamma, and beta distributions. For generating distributions of angles, the von Mises distribution is available.", "distributions of", 156),
        ("python demonstration. We also accept solutions that solve the problem in a more practical way, using whatever standard library functions are available. Please do not use any third party dependencies. These solutions should also be easy to understand and good examples of pythonic ways of doing things.", "I have no clue", -1),
        ("When the hash value of the pattern matches with the hash value of a window of the text but the window is not the actual pattern then it is called a spurious hit.Spurious hit increases the time complexity of the algorithm. In order to minimize spurious hit, we use modulus. It greatly reduces the spurious hit.", "helloworld", -1)
    ]
    test_cases_random = [
        ("AAAAAAAAAAAAAAA","BBA", -1),
    ]

    for _ in range(10):
        temp = random.choices(range(97, 123), k=random.randrange(10,20))
        random_str = "".join([chr(e) for e in temp])
        start = random.randrange(0, len(random_str) // 2)
        end = random.randrange(len(random_str)//2, len(random_str) + 1)
        test_cases_random.append((random_str, "asdf1dca", -1))
        test_cases_random.append((random_str, random_str[start:end], start))
    
    test_functions = [
        rabin_karp_search,
        knuth_morris_pratt_search,
        boyer_moore_search_bad_char
    ]
    
    def test_pattern_search(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)
        
        for _ in range(num_runs):
            for haystack, needle, expected in self.test_cases_random:
                for string_search in self.test_functions:
                    start = time.process_time()
                    assert(
                    string_search(haystack, needle) == expected
                    ), f"{string_search.__name__} failed at {haystack} looking for {needle}"
                    function_runtimes[string_search.__name__] += (
                    time.process_time() - start) * 1000
                    
        print(f"\n{num_runs} runs of random pattern")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<30}: {runtime:.1f}ms")
        
    def test_real_life_search(self):
        num_runs = 100
        function_runtimes = defaultdict(float)
        
        for _ in range(num_runs):
            for haystack, needle, expected in self.test_cases_real_life:
                for string_search in self.test_functions:
                    start = time.process_time()
                    assert(
                    string_search(haystack, needle) == expected
                    ), f"{string_search.__name__} failed at \n{haystack} \nlooking for: \n{needle}"
                    function_runtimes[string_search.__name__] += (
                    time.process_time() - start) * 1000
                    
        print(f"\n{num_runs} runs of real life passage")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<30}: {runtime:.1f}ms")
    
    
if __name__ == "__main__":
    unittest.main()