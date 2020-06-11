"""
In a sorted arr find the number which is greater than or equal to the asked number.
You can assume that the asked number will always be in the range of [ 0, arr[-1] ].

Example 1:
arr = [10, 15, 20, 25]
num = 7, ans = 10
num = 10, ans = 10
num = 13, ans = 15
num = 18, ans = 20
num = 21, ans = 25

Example 2:
arr = [2, 10, 20]
num = 0, ans = 2
num = 2, ans = 2
num = 8, ans = 10
num = 14, ans = 20
num = 20, ans = 20
"""


class Solution:
    def find_num_from_arr(self, arr, num, i, j):
        if i > j:
            return arr[j+1]
        mid = (i+j)//2
        if arr[mid] == num:
            return arr[mid]
        
        if num < arr[mid]:
            return self.find_num_from_arr(arr, num, i, mid-1)
        return self.find_num_from_arr(arr, num, mid+1, j)
        
    def get_next_equal_or_bigger_num_in_sorted_arr(self, arr, num):
        return self.find_num_from_arr(arr, num, 0, len(arr)-1)


a = Solution()
assert 10 == a.get_next_equal_or_bigger_num_in_sorted_arr([10, 15, 20, 25], 7)
assert 10 == a.get_next_equal_or_bigger_num_in_sorted_arr([10, 15, 20, 25], 10)
assert 15 == a.get_next_equal_or_bigger_num_in_sorted_arr([10, 15, 20, 25], 13)
assert 20 == a.get_next_equal_or_bigger_num_in_sorted_arr([10, 15, 20, 25], 18)
assert 25 == a.get_next_equal_or_bigger_num_in_sorted_arr([10, 15, 20, 25], 21)

assert 2 == a.get_next_equal_or_bigger_num_in_sorted_arr([2, 10, 20], 0)
assert 2 == a.get_next_equal_or_bigger_num_in_sorted_arr([2, 10, 20], 2)
assert 10 == a.get_next_equal_or_bigger_num_in_sorted_arr([2, 10, 20], 8)
assert 20 == a.get_next_equal_or_bigger_num_in_sorted_arr([2, 10, 20], 14)
assert 20 == a.get_next_equal_or_bigger_num_in_sorted_arr([2, 10, 20], 20)
