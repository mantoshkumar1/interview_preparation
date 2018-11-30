class MergeSort:
    def simple_mergesort(self, arr):
        len_arr = len(arr)
        if len_arr == 0 or len_arr == 1:
            return arr
        
        mid = len_arr // 2
        
        arr1 = self.simple_mergesort(arr[0:mid])
        arr2 = self.simple_mergesort(arr[mid:])
        
        return self.simple_merge(arr1, arr2)
        
    def simple_merge(self, a1, a2):
        a1_len = len(a1)
        a2_len = len(a2)

        sorted_arr = []
        i = j = 0
        
        while i < a1_len and j < a2_len:
            if a1[i] <= a2[j]:
                sorted_arr.append(a1[i])
                i += 1
            else:
                sorted_arr.append(a2[j])
                j += 1
                
        sorted_arr.extend(a1[i:])
        sorted_arr.extend(a2[j:])
        
        return sorted_arr

    def sort(self, arr):
        # this mergesort will sort the arr inplace, returning for testing purpose only
        self.mergesort(arr, 0, len(arr))
        return arr
    
    def mergesort(self, arr, i, j):
        if i == j or i + 1 == j:
            return
        
        mid = (i + j) // 2
        
        self.mergesort(arr, i, mid)
        self.mergesort(arr, mid, j)
        self.merge(arr, i, mid, j)
    
    def merge(self, arr, i, mid, j):
        ai, aj = i, mid
        
        bi, bj = mid, j
        
        merged_sorted_arr = []
        
        while ai < aj and bi < bj:
            if arr[ai] <= arr[bi]:
                merged_sorted_arr.append(arr[ai])
                ai += 1
            else:
                merged_sorted_arr.append(arr[bi])
                bi += 1
        
        while ai < aj:
            merged_sorted_arr.append(arr[ai])
            ai += 1
        
        while bi < bj:
            merged_sorted_arr.append(arr[bi])
            bi += 1
        
        arr[i:j] = merged_sorted_arr


s = MergeSort()

a = [1, 2, 3, 4]
assert [1, 2, 3, 4] == s.sort(a)

a = [4, 3, 2]
assert [2, 3, 4] == s.sort(a)

a = [9, 8, 7, 1, 2, 3]
assert [1, 2, 3, 7, 8, 9] == s.sort(a)


a = [1, 2, 3, 4]
assert [1, 2, 3, 4] == s.simple_mergesort(a)

a = [4, 3, 2]
assert [2, 3, 4] == s.simple_mergesort(a)

a = [9, 8, 7, 1, 2, 3]
assert [1, 2, 3, 7, 8, 9] == s.simple_mergesort(a)
