"""
First Missing Positive
https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array-set-2/

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

Approach:
We make the value at index corresponding to given array element equal to array element. For
example: consider the array = {2, 3, 7, 6, 8, -1, -10, 15}. To mark presence of element 2 in
this array, we make arr[2-1] = 2. In array subscript [2-1], 2 is element to be marked
and 1 is subtracted because we are mapping an element value range [1, N] on index value
range [0, N-1]. But if we make arr[1] = 2, we will loss data stored at arr[1]. To avoid
this, we first store value present at arr[1] and then update it. Next we will mark presence
of element previously present at arr[1], i.e. 3. Clearly this lead to some type of random
traversal over the array. Now we have to specify a condition to mark the end of this
traversal. There are three conditions that mark the end of this traversal:

1. If element to be marked is negative: No need to mark the presence of this element as
we are interested in finding the first missing positive integer. So if a negative element
is found, simply end the traversal as no more marking of presence of an element is done.

2. If element to be marked is greater than N : No need to mark the presence of this
element because if this element is present then certainly it has taken a place of an
element in range [1, N] in array of size N and hence ensuring that our answer lies in
the range[1, N]. So simply end the traversal as no more marking of presence of an element
is done.

3. If presence of current element is already marked: Suppose element to be marked present
is val. If arr[val-1] = val, then we have already marked the presence of this element.
So simply end the traversal as no more marking of presence of an element is done.
Also note that it is possible that all the elements of array in the range [1, N] are not
marked present in current traversal. To ensure that all the elements in the range are
marked present, we check each element of the array lying in this range. If element is
not marked, then we start a new traversal beginning from that array element.

After we have marked presence of all array elements lying in the range [1, N], we
check which index value ind is not equal to ind+1. If arr[ind] is not equal to ind+1,
then ind+1 is the smallest positive missing number. Recall that we are mapping index
value range [0, N-1] to element value range [1, N], so 1 is added to ind. If no such
ind is found, then all elements in the range [1, N] are present in the array. So the
first missing positive number is N+1.



How this solution works in O(n) time?
Observe that each element in range [1, N] is traversed at most twice in worst case.
First while performing a traversal started from some other element in the range.
Second when checking if a new traversal is required to be initiated from this element
to mark the presence of unmarked elements. In worst case each element in the
range [1, N] are present in the array and thus all N elements are traversed twice.
So total computations are 2*n, and hence the time complexity is O(n).
"""


class Solution:
    def swap(self, nums, i, j):
        if i >= len(nums) or j >= len(nums):
            return
        
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, 0)
        
        num_len = len(nums)
        
        for index in range(num_len):
            #print(index, nums[index])
            if nums[index] == index or nums[index] <= 0 or \
                    nums[index] >= num_len or nums[index] == nums[nums[index]]:
                continue
            
            while True:
                self.swap(nums, index, nums[index])
                if nums[index] == index or nums[index] <= 0 or \
                        nums[index] >= num_len or nums[index] == nums[nums[index]]:
                    break
        
        print(*nums, sep="  ")
        for index in range(num_len):
            if index != nums[index]:
                return index
        
        return index+1
        
        
a = Solution()
assert 4 == a.firstMissingPositive([1, 2, 3])
assert 3 == a.firstMissingPositive([0, 2, 2, 1, 1])
assert 2 == a.firstMissingPositive([1, 1000])
assert 2 == a.firstMissingPositive([3, 4, -1, 1])
assert 1 == a.firstMissingPositive([2])
assert 1 == a.firstMissingPositive([])
assert 2 == a.firstMissingPositive([-10, -3, -100, -1000, -239, 1])









