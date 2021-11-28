def solution(s, t):
    count = 0
    s_digits = []
    small = []
    big = []
    t_digits = []
    i = j = 0

    while i < len(s) and s[i] == t[i] and 'a' <= s[i] <= 'z':
        i += 1
    
    for c in range(i - 1, len(s)):
        if s[c].isdigit():
            s_digits.append(c)
        small.append(s[c])
    
    for c in range(i - 1, len(t)):
        if t[c].isdigit():
            t_digits.append(c)
        big.append(t[c])

    for c in s_digits:
        if small[:c] + small[c + 1:] < big:
            count += 1

    for c in t_digits:
        if small < big[:c] + big[c + 1:]:
            count += 1
    print(s_digits, t_digits)
    return count

print(solution("ab12c", "ab24z")) 