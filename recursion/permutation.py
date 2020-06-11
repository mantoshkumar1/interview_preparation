num_perm = 0  # used for permutation method


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
        permutation(s, n, r, curr_r + 1, one_perm)
        one_perm.pop()


class Solution:
    def get_one_ans(self, nums, visited):
        return list(map(lambda x: nums[x], visited))

    def utils(self, nums, r, visited=[]):
        if r == 0:
            return [self.get_one_ans(nums, visited)]

        ans = []

        for i in range(len(nums)):
            if i in visited:
                continue

            visited.append(i)
            ans += self.utils(nums, r - 1, visited)
            visited.pop()

        return ans

    def other_permutation_method(self, arr, r):
        return self.utils(arr, r)


s = "abcd"
n = len(s)
r = 3

permutation(s, n, r, 0)

import itertools

assert num_perm == len(list(itertools.permutations(s, r)))

obj = Solution()
obj.other_permutation_method(s, r)
