"""
http://ruslanledesma.com/2016/02/14/adjacent-coins.html
https://stackoverflow.com/questions/50357387/wrong-answer-in-task-mistake-in-algorithm

The Adjacent Coins Problem:
----------------------------
Consider N coins aligned in a row. Each coin is showing either heads (1) or tails (0).
The adjacency of these coins is the number of pairs of adjacent coins showing
the same face. Return the maximum possible adjacency that can be obtained by
reversing one coin. Remember one of the coin MUST be reversed.

For example:
1 1 0 1 0 0
and after change third we get 1 1 1 1 0 0 so we have 4 pairs.

Explanation:
------------
The key point is, “one of the coins MUST be reversed”. It means, we HAVE to flip a coin,
that’s the requirement of the question. Thus for a test case where all the coins have the
same face, for example: [0, 0] or [1, 1] then the initial max adjacency would be 1, but
when we flip a coin, then new max adjacency would become 0, which must be covered by the code.

For other test cases, it should calculate the max change (0, 1, 2) that might occur for
each flip and eventually adds the max new change (among all possible flips) and adds with initial adjacency.
"""


def Solution(A):
    n = len(A)
    ans = 0

    for i in range(n - 1):
        if A[i] == A[i + 1]:
            ans += 1

    # if whole array is equal then max Adjacency after flip can only be
    # achieved if we flip either the first or last element.
    if ans == n - 1:
        return ans - 1

    max_flip_adjacency = 0

    # this is for each flip
    for i in range(n):
        r = 0

        if i > 0:
            # Early state - State after flip - Adjacency (Depending upon State after flip)
            # Equal       - Not equal        : -1
            # Not equal   - Equal            : +1
            if A[i] == A[i - 1]:
                r -= 1
            else:
                r += 1

        if i < n - 1:
            if A[i] == A[i + 1]:
                r -= 1
            else:
                r += 1

        max_flip_adjacency = max(max_flip_adjacency, r)

    return ans + max_flip_adjacency


arr = [1, 1, 0, 1, 0, 0]
ans = Solution(arr)
assert ans == 4

arr = [1, 1, 1, 1]
ans = Solution(arr)
assert ans == 2

arr = [0, 0, 0, 0]
ans = Solution(arr)
assert ans == 2

arr = [1, 0, 1, 1]
ans = Solution(arr)
assert ans == 3

arr = [1, 1, 1, 0]
ans = Solution(arr)
assert ans == 3

arr = [1, 1, 0, 1]
ans = Solution(arr)
assert ans == 3

arr = [0, 1, 1, 1]
ans = Solution(arr)
assert ans == 3

arr = [1, 0, 0, 1]
ans = Solution(arr)
assert ans == 2

arr = [1, 1, 0, 0]
ans = Solution(arr)
assert ans == 2

arr = [0, 0, 1, 1]
ans = Solution(arr)
assert ans == 2
