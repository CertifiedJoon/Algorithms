def merge(s1, s2, s):
    i = j = 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i + j] = s1[i]
            i += 1
        else:
            s[j + i] = s2[j]
            j += 1

def merge_sort(s):
    n = len(s)
    if n < 2:
        return
    mid = n // 2
    s1 = s[0: mid]
    s2 = s[mid: n]
    
    merge_sort(s1)
    merge_sort(s2)

    merge(s1, s2, s)

def bottom_up_merge_sort(s):
    n = len(s)
    logn = math.ceil(math.log(n,2))
    src, dest = S, [None] * n 
    for i in (2**k for k in range(logn)):
        for j in range(0, n, 2*i):
            merge(src, dest, j, i)
        src, dest = dest, src
    if s is not src:
        s[0:n] = src[0:n]

def quick_sort(s):

def quick_sort(s, l, r):
    if l >= r:
        return
    mid = l + (r // 2)
    s[mid], s[l] = s[l], s[mid]
    last = 0
    i = l
    while i < r - l:
        if s[i] < s[l]:
            last += 1
            s[last], s[i] = s[i], s[last]
    s[last], s[l] = s[l], s[last]
    quick_sort(s, mid - 1)
    quick_sort(mid + 1, r)