num_perm = 0


def permutation(s, n, r, curr_r, one_perm=[]):
    if curr_r == r:
        global num_perm
        num_perm += 1
        print(one_perm)
        return
    
    for i in range(0, n):
        if s[i] in one_perm:
            continue
            
        one_perm.append(s[i])
        permutation(s, n, r, curr_r+1, one_perm)
        one_perm.pop()


s = "abcd"
n = len(s)
r = 3

permutation(s, n, r, 0)

import itertools
assert num_perm == len(list(itertools.permutations(s, r)))



