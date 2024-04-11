from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        arr = [self.val]
        while self.next:
            self = self.next
            arr.append(self.val)
        return str(arr)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        reversed = ListNode(head.val)
        while head and head.next:
            head.val, head.next = head.next.val, head.next.next
            reversed = ListNode(head.val, reversed)
        return reversed


if __name__ == "__main__":
    s = Solution()
    linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = s.reverseList(linked_list)
    print(res)

    linked_list = []
    res = s.reverseList(linked_list)
    print(res)

    linked_list = ListNode(1)
    res = s.reverseList(linked_list)
    print(res)