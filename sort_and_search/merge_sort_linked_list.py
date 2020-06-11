class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        return str(self.val)
        

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __eq__(self, other):
        h1 = self.head
        h2 = other.head
        
        while h1 and h2:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        
        if h1 or h2:
            return False
        
        return True
    """
    def __ne__(self, other):
        return not self.__eq__(other)
    """
    def __gt__(self, other):
        h1 = self.head
        h2 = other.head
    
        while h1 and h2:
            if h1.val > h2.val:
                return True
            h1 = h1.next
            h2 = h2.next
        
        if h1 and not h2:
            return True
        
        return False

    def __ge__(self, other):
        h1 = self.head
        h2 = other.head
    
        while h1 and h2:
            if h1.val > h2.val:
                return True
            h1 = h1.next
            h2 = h2.next
    
        if not h1 or not h2:
            return True
        
        if h1 and not h2:
            return True
    
        return False

    def append(self, val):
        tmp = self.head
        if tmp is None:
            self.head = Node(val)
            return
        
        while tmp.next:
            tmp = tmp.next
        
        tmp.next = Node(val)
        
    def insert(self, arr):
        for i in arr:
            self.append(i)
    
    def merge_sorted_linked_list(self, L1, L2):
        if not L1:
            return L2
        
        if not L2:
            return L1
        
        if L1.val <= L2.val:
            tmp = L1
            L1 = L1.next
        else:
            tmp = L2
            L2 = L2.next
            
        tmp.next = self.merge_sorted_linked_list(L1, L2)
        return tmp
    
    def divide_linked_list(self, head):
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        partition = slow.next
        slow.next = None
        
        return head, partition
        
    def mergesort(self, head):
        if head is None or head.next is None:
            return head
        
        L1, L2 = self.divide_linked_list(head)
        
        L1 = self.mergesort(L1)
        L2 = self.mergesort(L2)
        
        """ to understand uncomment it
        print("L1", end=": ")
        self.display(L1)
        print("L2", end=": ")
        self.display(L2)
        """
        
        return self.merge_sorted_linked_list(L1, L2)
        
    def sort(self):
        # necessary to reassign as original linked list has been modified
        self.head = self.mergesort(self.head)
    
    def display(self, head):
        tmp = head
        while tmp:
            print(tmp.val, end=" - ")
            tmp = tmp.next
            
        print("")

 
ll = LinkedList()
ll.insert([5, 4, 3, 2, 1])
ll.sort()

print("sorted list: ", end=": ")
ll.display(ll.head)

# just experimenting with equator
tll = LinkedList()
tll.insert([1, 2, 3, 4 ,5, 6])
assert ll != tll

tll = LinkedList()
tll.insert([1, 2, 3, 4 ,5])
assert ll == tll

tll = LinkedList()
tll.insert([10, 2, 3, 4 ,5])
assert tll > ll
assert ll < tll
assert tll >= ll
assert ll <= tll


