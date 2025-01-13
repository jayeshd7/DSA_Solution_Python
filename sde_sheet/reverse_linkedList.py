from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev

if __name__ == '__main__':

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    s = Solution()
    reversed_head = s.reverseList(head)
    while reversed_head:
        print(reversed_head.val)
        reversed_head = reversed_head.next