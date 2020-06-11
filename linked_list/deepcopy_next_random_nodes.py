"""
Given a linked list with two reference node and a val, return a deepcopied linked list.
One reference node as usual points to next node, while the other reference node points
to a random node in the linked list
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = self.random = None

    def __repr__(self):
        return "{}  ".format(self.val)


def deepcopy(head):
    if not head:
        return None

    d = dict()

    new_head = Node(head.val)
    d[head] = new_head

    tmp_node = head.next
    tmp_new_node = new_head

    # linking next nodes
    while tmp_node:
        tmp_new_node.next = Node(tmp_node.val)
        d[tmp_node] = tmp_new_node.next

        tmp_new_node = tmp_new_node.next
        tmp_node = tmp_node.next

    tmp_new_node = new_head

    # linking random nodes
    while head:
        random_node = head.random
        if random_node in d:
            tmp_new_node.random = d[random_node]

        head = head.next
        tmp_new_node = tmp_new_node.next

    return new_head


def test(head, new_head):
    while head:
        assert head.val == new_head.val
        if head.next:
            assert head.next.val == new_head.next.val

        if head.random:
            assert head.random.val == new_head.random.val

        head = head.next
        new_head = new_head.next


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next

    new_head = deepcopy(head)

    test(head, new_head)
