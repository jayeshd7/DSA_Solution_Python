from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)

    s = Solution()
    print(s.isPalindrome(head))  # Output: True
