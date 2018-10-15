def combination(s, n, r, curr_i, curr_r, op=[]):
    if r == curr_r:
        print(op)
        return
    
    for i in range(curr_i, n):
        op.append(s[i])
        combination(s, n, r, i+1, curr_r+1, op)
        op.pop()
    return


s = "abc"
n = len(s)
r = 2
combination(s, n, r, 0, 0)
