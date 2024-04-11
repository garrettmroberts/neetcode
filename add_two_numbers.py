from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carryover: Optional[int] = 0) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        curr = dummy_head
        carrover = 0
        while l1 is not None or l2 is not None:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            sum = l1Val + l2Val + carryover
            carryover = sum // 10
            new_node = ListNode(sum % 10)
            curr.next = new_node
            curr = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy_head.next
    

if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    print(Solution().addTwoNumbers(l1, l2))
