from typing import List, Optional


"""
Singly Linked List Implementation using a dummy node for simpler implementation

Useful for: retrieving first and last inserted elemenets, quick insertion, quick deletion

Space: O(n), n is n the number of nodes in the Linked List. Storing value and next pointer in each node.

Time:
Search: O(n)
Insertion: O(1) at the head and tail, O(n) for specific elements or indexes
Deletion: O(1) at the head and tail, O(n) for specific elements or indexes
Traversal: O(n)
"""


class Node:
    def __init__(self, value):
        self.value: int = value 
        self.next: Optional[Node] = None 

class LinkedList:
    
    def __init__(self):
        self.size = 0
        # Dummy node to make life easier when the LL is empty
        self.head = Node(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        # Traverse the linked list as long as the curr node isn't None
        while curr: 
            if i == index: 
                return curr.value
            # Traverse to the node at the next pointer and update our index
            i += 1 
            curr = curr.next
        return -1
            

    def insertHead(self, val: int) -> None:
        # Create new node for the input value
        newNode = Node(val)
        # Update the size
        self.size += 1
        # Track prev head
        prevHead = self.head.next
        # Update new node's next pointer to our previous head
        newNode.next = prevHead
        # Make new value the head node 
        self.head.next = newNode
        # If the next pointer of our new node is None (inserted into empty LL)
        if newNode.next is None:
            self.tail = newNode


    def insertTail(self, val: int) -> None:        
        self.size += 1 
        # Make prev tail point to the new node
        self.tail.next = Node(val)
        # Make the new node the tail
        self.tail = self.tail.next
         

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        # Find previous node of node to remove
        # Start at dummy node to cover empty LL case
        while i < index and curr:
            i += 1
            curr = curr.next

        # If the previous node to to the node to remove exists and it
        # points to a non-None node, continue removing
        if curr and curr.next:
            # Make the current node the tail if we are deleting the tail node
            if curr.next == self.tail:
                self.tail = curr
            # Point the current node to what the next node's next pointer was pointing too
            # Ex. 1 -> 2 -> 3, now becomes 1 -> 3 
            curr.next = curr.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        items = []

        if self.size == 0:
            return items
        
        i = 0
        curr = self.head.next
        # Traverse the linked list as long as we don't exceed the size and
        # the current node isn't nonexistent
        while curr:
            items.append(curr.value)
            # Traverse to the node at the next pointer and update our index
            i += 1 
            curr = curr.next        
        return items
        

