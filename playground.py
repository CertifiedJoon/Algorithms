import random
test_cases_random = []
    
for _ in range(10):
    temp = random.choices(range(97, 123), k=random.randrange(10,20))
    random_str = "".join([chr(e) for e in temp])
    start = random.randrange(0, len(random_str) // 2)
    end = random.randrange(len(random_str)//2, len(random_str) + 1)
    test_cases_random.append((random_str, random_str[start:end], True))
    test_cases_random.append((random_str, "asdf1dca", False))
        
print(test_cases_random)