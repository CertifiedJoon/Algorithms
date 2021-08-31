def boyer_moore_search_good_char(haystack, needle):
    s = 0
    m = len(haystack)
    n = len(needle)
    bpos = [0] * (n + 1)
    shift = [0] * (n + 1)
    
    process_good_char_heuristics(bpos, shift, needle, n)
    process_complete_shift(bpos, shift, n)
    
    while s <= (m - n):
        print(s)
        j = n - 1
        
        while j >= 0 and haystack[s + j] == needle[j]:
            print(f"\t {j}")
            j -= 1
        
        if j < 0:
            return s
        
        else:
            s += shift[j + 1]      
    return -1
    
def process_good_char_heuristics(bpos, shift, needle, n):
    i = n 
    j = n + 1
    bpos[i] = j
    while i > 0:
        while j <= n and needle[i - 1] != needle[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i 
            else:
                j = bpos[j]
        i -= 1
        j -= 1
        bpos[i] = j 

def process_complete_shift(bpos, shift, m):
    j = bpos[0]
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = bpos[j]
            
if __name__ == "__main__":
    print(boyer_moore_search_good_char("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut posuere nisi elementum justo rhoncus sollicitudin. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Suspendisse vitae nunc metus. Vestibulum mattis, lectus non accumsan fringilla, dolor augue viverra arcu, quis sagittis sapien massa id augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Fusce mattis ac sem non sagittis. Sed ac iaculis tortor, lobortis interdum dolor. Aliquam eget sodales tortor. In rutrum faucibus libero, a laoreet sapien cursus non. Integer vulputate lorem id risus fringilla feugiat. Pellentesque molestie dapibus pharetra. Nam vestibulum lorem at tempor gravida. Maecenas tortor sem, molestie non pretium sit amet, consequat in ipsum. In sed rutrum tortor. Duis consequat nisi non scelerisque finibus. Nam eu imperdiet mi. Donec leo nulla, eleifend et posuere id, accumsan consectetur erat. Nam viverra risus turpis, ultrices feugiat metus eleifend ac. Mauris ultrices, felis in pulvinar egestas, magna arcu convallis metus, nec cursus enim nisi eget lacus. Pellentesque quis diam in ligula faucibus tincidunt in at urna. Pellentesque sit amet leo et felis facilisis semper. Curabitur bibendum nulla id tellus lacinia accumsan. Ut nisi orci, laoreet ac vestibulum ut, ornare sed metus. Proin accumsan vestibulum nisi, in bibendum risus commodo sit amet. Aliquam pretium vestibulum dictum. Vivamus fermentum tellus eget massa faucibus, eu blandit urna commodo. Suspendisse varius urna leo, congue ultricies nibh cursus nec. Fusce sit amet augue malesuada, tristique augue non, ullamcorper augue. Aenean ut neque tristique, ullamcorper felis id, maximus lorem. Vivamus molestie auctor metus, ac ornare ligula vehicula vitae. Aenean suscipit semper lobortis. Pellentesque nisl velit, posuere sed lacus vitae, congue tincidunt justo. Nam non orci vel nunc consectetur bibendum quis sit amet nibh. Curabitur nec nibh bibendum, tempus turpis sit amet, hendrerit lorem. Vivamus fermentum posuere lacus ut sollicitudin. Integer varius luctus purus, ac ultricies neque semper vel. Nam convallis justo iaculis libero interdum, at efficitur mauris dictum. Vivamus a quam vitae metus euismod dapibus nec quis lectus. Aliquam sollicitudin sem at dui mattis, in elementum ligula vestibulum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tempor mauris justo, at vulputate tortor dictum nec. Morbi molestie posuere turpis, ac lobortis lorem. Maecenas massa dolor, pharetra in tellus vitae, convallis dictum orci. Proin eu erat nisi. Ut placerat urna ac orci venenatis facilisis. Nullam in ante odio. Integer vel est eget odio dapibus aliquam et at lacus. Nullam libero ante, posuere et molestie et, sodales rutrum ex. Proin mollis turpis non massa posuere varius. Nullam bibendum lacus non purus auctor suscipit. Curabitur erat dolor, tempus sed erat a, gravida euismod neque. Sed est orci, rhoncus eu cursus eget, finibus vitae sapien. Maecenas feugiat augue vitae vulputate aliquam. In tempor, libero ac lobortis dictum, leo est lacinia sem, ac sagittis risus urna auctor nulla. In a iaculis nunc.","In a iaculis nunc"))
    
    