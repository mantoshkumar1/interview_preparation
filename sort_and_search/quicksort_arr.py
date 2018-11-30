class QuickSort:
    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    
    def partition(self, arr, i, j):
        pivot = i
        while i < j:
            while i < j and arr[i] <= arr[pivot]:
                i += 1
            while i <= j and arr[j] >= arr[pivot]:
                j -= 1
                
            if i < j:
                self.swap(arr, i, j)
        
        self.swap(arr, pivot, j)
        
        return j
    
    def quicksort(self, arr, i, j):
        if i >= j:
            return
        
        p = self.partition(arr, i, j)
        self.quicksort(arr, i, p - 1)
        self.quicksort(arr, p + 1, j)
    
    def sort(self, arr):
        # this quicksort will sort the arr inplace, returning for testing purpose only
        self.quicksort(arr, 0, len(arr) - 1)
        return arr


s = QuickSort()

a = [1, 2, 3, 4]
assert [1, 2, 3, 4] == s.sort(a)

a = [4, 3, 2, 1]
assert [1, 2, 3, 4] == s.sort(a)

a = [9, 8, 7, 1, 2, 3]
assert [1, 2, 3, 7, 8, 9] == s.sort(a)
