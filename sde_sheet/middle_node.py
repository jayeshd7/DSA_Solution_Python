from typing import Optional


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    s = Solution()
    middle_node = s.middleNode(head)
    print(middle_node.value)  # Output: 3
