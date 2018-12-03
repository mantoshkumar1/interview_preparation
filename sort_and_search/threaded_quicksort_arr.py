import threading
import queue


class QuickSort:  # Producer-Consumer Problem
    def __init__(self, nth):
        self.arr = None
        self.nth = nth  # number of threads
        self.quicksort_th_list = []  # reference to created threads - will be used to wait for them
        
        self.queue_ij = queue.Queue()  # will be consumed by threads
        
    def create_quicksort_threads(self):
        for i in range(self.nth):
            th_instance = threading.Thread(target=self.quicksort, daemon=True)
            self.quicksort_th_list.append(th_instance)
            th_instance.start()
    
    def release_quicksort_threads(self):
        for i in range(self.nth):
            self.quicksort_th_list[i].join()
            
    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        
    def partition(self, i, j):
        pivot = i
        while i < j:
            while i < j and self.arr[i] <= self.arr[pivot]:
                i += 1
            while i <= j and self.arr[j] >= self.arr[pivot]:
                j -= 1
                
            if i < j:
                self.swap(i, j)
        
        self.swap(pivot, j)
        
        return j
    
    def quicksort(self):
        while True:
            try:
                i, j = self.queue_ij.get()
            except queue.Empty:
                break
            
            if i >= j:
                break
            
            p = self.partition(i, j)
            
            self.queue_ij.put((i, p-1))
            self.queue_ij.put((p + 1, j))
            
            #self.quicksort(self.arr, i, p - 1)
            #self.quicksort(self.arr, p + 1, j)
    
    def sort(self, arr):
        self.arr = arr
        
        # this quicksort will sort the arr inplace, returning for testing purpose only
        # self.quicksort()
        
        # initialize self.queue_ij
        self.queue_ij.put((0, len(arr) - 1))

        # start threads
        self.create_quicksort_threads()
        
        # gracefully waits for running threads
        self.release_quicksort_threads()

        return self.arr


s = QuickSort(nth=4)

a = [1, 2, 3, 4]
assert [1, 2, 3, 4] == s.sort(a)

a = [4, 3, 2, 1]
assert [1, 2, 3, 4] == s.sort(a)

a = [9, 8, 7, 1, 2, 3]
assert [1, 2, 3, 7, 8, 9] == s.sort(a)
