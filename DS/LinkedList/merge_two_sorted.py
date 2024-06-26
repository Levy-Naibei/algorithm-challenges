
"""
Given pointers to the heads of two sorted linked lists, 
merge them into a single, sorted linked list.
Either head pointer may be null meaning that the corresponding list is empty.
"""
class Node:
    def __init__(self, data):
        self.data = data

def mergeLists(head1, head2):
    # starting point of merged list
    dummy = Node(-1)
    current = dummy

    # Iterates through both lists as long as neither is empty
    while head1 and head2:
        if head1.data < head2.data:
            # Appends the l1 node to the merged list.
            current.next = head1
            # Moves the l1 pointer to the next node.
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        # Appends the remaining nodes to the merged list
        current = current.next

    # Returns the merged list starting from the node next to the dummy node.
    current.next = head2 or head1
    return dummy.next
