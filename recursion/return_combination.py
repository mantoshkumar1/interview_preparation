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


def other_combination_method(arr, n, curr_r, curr_i, t_arr=[]):
    if curr_r == 0:
        return [t_arr.copy()]

    op = []
    for i in range(curr_i, n):
        t_arr.append(arr[i])
        op += other_combination_method(arr, n, curr_r - 1, i + 1, t_arr)
        t_arr.pop()

    return op


s = "abc"
n = len(s)
r = 2
all_comb = []
combination(s, n, r, 0, 0, all_comb)

a2 = other_combination_method(s, n, r, 0)
print(all_comb)

assert all_comb == a2
