# choose items randomly from a dict based on their count
# d = {'a': 9, 'b': 1} then 'a' should be produced 9 out of 10 times and 'b' should be
# produced 1 out of 10 times

import random
from collections import defaultdict


class SolutionApproach2:
    def __init__(self, d):
        random.seed(1245)  # integer starting value used in generating random numbers: optional
        self.total_sum = sum(d.values())
        self.random_num_generator = self.int_generator()
        self.arr = self.create_sorted_arr(d)  # [(NUM, 'a')]
        self.count = 0

        # just for personal purpose to see what got printed how many time
        self.printed_chars_count = defaultdict(lambda: 0)
    
    def create_sorted_arr(self, d):
        arr = []
        sum_upto = 0
        
        for k, v in d.items():
            sum_upto = sum_upto + v
            arr.append((sum_upto + v, k))
        
        return arr
    
    def int_generator(self):
        max_val = self.total_sum
        while True:
            yield random.randint(1, max_val)
    
    # look into code of get_next_num_in_sorted_arr.py
    def get_next_equal_or_bigger_number_from_sorted_arr(self, num, i, j):
        if i > j:
            return self.arr[j + 1]
        
        mid = (i + j) // 2
        
        if self.arr[mid][0] == num:
            return self.arr[mid]
        
        if num < self.arr[mid][0]:
            return self.get_next_equal_or_bigger_number_from_sorted_arr(num, i, mid - 1)
        
        return self.get_next_equal_or_bigger_number_from_sorted_arr(num, mid + 1, j)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.count < self.total_sum:
            random_int = self.random_num_generator.__next__()
            arr_entry = self.get_next_equal_or_bigger_number_from_sorted_arr(
                                                    random_int, 0, len(self.arr) - 1)
            self.count += 1
            
            self.printed_chars_count[arr_entry[1]] += 1
            return arr_entry[1]
        
        raise StopIteration


class Solution:
    def gcd(self, a, b):
        while a != 0:
            tmp = a
            a = b % a
            b = tmp
        return tmp
    
    def gcd_of_dict_values(self, d):
        # if a=10, b =90; we could get the same result if we say a=1, and b =9
        v = list(d.values())
        a = v[0]
        d_len = len(d)
        
        for i in range(1, d_len):
            a = self.gcd(a, v[i])
            if a == 1:
                break
        
        return a
    
    def __init__(self, d):
        random.seed(98643)  # integer starting value used in generating random numbers: optional
        self.greatest_common_values_divisor = self.gcd_of_dict_values(d)
        self.arr = self.create_arr(d)
        
        self.count = sum(d.values())
        self.random_num_generator = self.int_generator()
        self.curr = 0
        
        # just for personal purpose to see what got printed how many time
        self.printed_chars_count = defaultdict(lambda: 0)
    
    def create_arr(self, d):
        arr = []
        for k, v in d.items():
            v = v // self.greatest_common_values_divisor
            tmp = [k] * v
            arr.extend(tmp)
        return arr
    
    def int_generator(self):
        l_arr = len(self.arr)
        while True:
            yield random.randint(0, l_arr - 1)  # randint generates random int in range [i, j]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.curr < self.count:
            n = self.random_num_generator.__next__()
            self.curr += 1
            self.printed_chars_count[self.arr[n]] += 1
            return self.arr[n]
        
        raise StopIteration


d = {'a': 3, 'b': 9, 'c': 7}
a = Solution(d)
for _ in range(sum(d.values())):
    print(a.__next__(), end="  ")

print()
print(a.printed_chars_count)


print("# ---------------------------------#")
print("Answer of another Approach: Binary search")
b = SolutionApproach2(d)
for _ in range(sum(d.values())):
    print(b.__next__(), end="  ")
    
print("")
print(a.printed_chars_count)
