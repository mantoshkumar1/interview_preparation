def combination(s, n, r, curr_i, curr_r, all_comb, op=[]):
    if r == curr_r:
        # without copy when op gets changes due to pop, all_comb also changes
        
        # this also works
        # all_comb += [op.copy()]
        
        all_comb.append(op.copy())
        return
    
    for i in range(curr_i, n):
        op.append(s[i])
        combination(s, n, r, i + 1, curr_r + 1, all_comb, op)
        op.pop()
    
    return


s = "abc"
n = len(s)
r = 2
all_comb = []

combination(s, n, r, 0, 0, all_comb)
print(all_comb)