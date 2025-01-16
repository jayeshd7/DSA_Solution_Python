from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            current.next = ListNode(carry)

        return dummy.next

    def print_list(self, head):
        while head:
            print(head.val)
            head = head.next
if __name__ == '__main__':
    head1 = ListNode(2)
    head1.next = ListNode(4)
    head1.next.next = ListNode(3)

    head2 = ListNode(5)
    head2.next = ListNode(6)
    head2.next.next = ListNode(4)

    s = Solution()
    added_head = s.addTwoNumbers(head1, head2)
    s.print_list(added_head)  # Output: 7 0 8